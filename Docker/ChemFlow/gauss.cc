
#include <iostream>
#include "gauss.h"
#include <assert.h>

// #define DEBUG_ELIMINATION
// #define DEBUG_BELONGSTO

using namespace std;

template <class T>
inline void SWAP(T &a, T &b)
{
  T c;
  c = a;
  a = b;
  b = c;
}

template <class T>
inline T ABS(T a)
{
  return (a<0) ? -a : a;
}

template <class T>
inline int SIGN(T a)
{
  return (a<0) ? -1 : 1;
}

long gcd(long a, long b)
{
  while (b) {
    long t = b;
    b = a % b;
    a = t;
  }
  return a;
}

long lcm(long a, long b)
{
  a = ABS(a);
  b = ABS(b);
  return (a*b) / gcd(a,b);
}

/**
  Zero out a vector element, by adding a multiple of another vector.
  I.e., perform V = a * V + b * W,
  where V is our vector of interest, to make V[t] = 0.
  W is the vector we can use to cancel out the element, and the scalars
  a and b are determined to make V[t]=0.

  @param  t         Element of the vector to zero
  @param  vlen      Vector lengths
  @param  update    Vector to modify
  @param  selected  Vector to use to zero the element
*/
void cancelByRow(unsigned t, unsigned vlen, int* update, const int* selected)
{
  if (0==update) return;
  if (0==update[t]) return; 
  assert(selected[t]);
  if (0==selected[t]) return;
  long L = lcm(update[t], selected[t]);
  long a = ABS(L / update[t]);
  long b = ABS(L / selected[t]);
  if (SIGN(update[t]) == SIGN(selected[t])) b *= -1;
  for (unsigned i=0; i<vlen; i++) {
    update[i] *= a;
    update[i] += b * selected[i];
  }
}

void normalizeRow(int* row, unsigned pplust)
{
  if (0==row) return;
  long g = 0;
  bool neg = false;
  unsigned i;
  for (i=0; i<pplust; i++) {
    if (row[i]) break;
  }
  if (i>=pplust) return;  // zero row

  neg = row[i] < 0;
  g = row[i];

  for (++i; i<pplust; ++i) {
    if (0==row[i]) continue;
    g = gcd(g, row[i]);
  }

  if (neg) {
    g = -ABS(g);
  } else {
    g = ABS(g);
  }
  for (unsigned i=0; i<pplust; i++) {
    row[i] /= g;
  }
}

void showRow(std::ostream &out, const int* row, unsigned place, unsigned trans)
{
  if (0==row) return;
  out << "\t";
  bool printed = false;
  const unsigned pplust = place + trans;
  for (unsigned i=0; i<pplust; i++) {
    if (0==row[i]) continue;
    if (row[i] < 0) {
      out << "- ";
      if (row[i] < -1) out << -row[i];
      if (i<trans) {
        out << "T" << i+1 << " ";
      } else {
        out << "P" << i-trans+1 << " ";
      }
      printed = true;
      continue;
    }
    if (printed) out << "+ ";
    printed = true;
    if (row[i] > 1) {
      out << row[i];
    }
    if (i<trans) {
      out << "T" << i+1 << " ";
    } else {
      out << "P" << i-trans+1 << " ";
    }
  }
  out << "\n";
}

void matrixElimination(int** matrix, unsigned places, unsigned trans, unsigned& supplement)
{
  supplement = places;

#ifdef DEBUG_ELIMINATION
  cout << "Eliminating PT potion of matrix:\n";
  dumpMatrix(matrix, places, trans, supplement);
#endif
  for (unsigned t=0; t<trans; t++) {
#ifdef DEBUG_ELIMINATION
    cout << "\nTransition T" << t+1 << "\n\n";
#endif

    int row = -1;
    for (int p=supplement-1; p>=0; p--) if (matrix[p]) {
      if (0==matrix[p][t]) continue;
      row = p;
      break;
    }
    if (row<0) {
      //
      // Everything already canceled;
      // but we need to negate any of these vars
      // in the supplemental equations
      //
      for (unsigned p=supplement; p<places; p++) if (matrix[p]) {
        matrix[p][t] *= -1;
      }
      continue; 
    }
#ifdef DEBUG2_ELIMINATION
    cout << "canceling with row " << row << "\n";
#endif

    //
    // Use this row to cancel all others
    //
    for (int p=0; p<places; p++) {
      if (p != row) cancelByRow(t, places+trans, matrix[p], matrix[row]);
    }

    //
    // Put this row at the end, 
    // with negated transition column
    //
    matrix[row][t] *= -1;
    supplement--;
    if (row != supplement) {
      SWAP(matrix[row], matrix[supplement]);
    }

#ifdef DEBUG_ELIMINATION
    dumpMatrix(matrix, places, trans, supplement);
#endif
  }
  for (unsigned r=0; r<places; r++) {
    normalizeRow(matrix[r], places+trans);
  }
#ifdef DEBUG_ELIMINATION
  cout << "Final matrix:\n";
  dumpMatrix(matrix, places, trans, supplement);
#endif
}


void dumpMatrix(int** matrix, unsigned places, unsigned trans, unsigned supplement)
{
  if (0==matrix) {
    cout << "null matrix\n";
    return;
  }
  for (unsigned i=0; i<places; i++) {
    if (i==supplement) {
      cout << "--------------------\n";
    }
    if (0==matrix[i]) {
      cout << "[ null row ]\n";
    } else {
      cout << "[ ";
      for (unsigned j=0; j<trans + places; j++) {
        if (trans == j) cout << "| ";
        if (matrix[i][j]>=0) cout << " ";
        cout << matrix[i][j] << " ";
      }
      cout << "]\n";
    }
  }
}

/* ============================================================ */

/*
  New simpler method: just standard Gaussian Elimination
*/

void matrixElimStd(int** matrix, unsigned trans, unsigned places)
{
#ifdef DEBUG_ELIMINATION
  cout << "Starting Gaussian Elimination on matrix:\n";
  dumpMatrix(matrix, places, trans, places);
#endif

  unsigned col; // column to eliminate
  unsigned row = 0; // row we're using to eliminate
  for (col=0; col<trans+places; col++) {
    if (row >= places) break;

    //  Find 'best' row to eliminate this column:
    //    smallest magnitude, non-zero integer coefficient.
    unsigned bestrow = trans+places;    // invalid row
    for (unsigned r = row; r<places; r++) {
      if (0==matrix[r][col]) continue;
      if (bestrow >= trans+places) {
        bestrow = r;
        continue;
      }
      // see which is better
      if ( ABS(matrix[bestrow][col]) > ABS(matrix[r][col]) ) {
        bestrow = r;
      }
    } // for r

    // If no non-zero rows, then the column is already eliminated.
    // Go to the next column in that case.
    if (bestrow >= trans+places) continue;

#ifdef DEBUG_ELIMINATION
    cout << "Using row " << bestrow << " to zero out column " << col << "\n"; 
#endif

    // Put the best row 'first' by swapping rows
    if (bestrow > row) {
      SWAP(matrix[row], matrix[bestrow]);
    }

    // Cancel all other rows by this row
    for (unsigned r = 0; r<places; r++) {
      if (r != row) {
        cancelByRow(col, trans+places, matrix[r], matrix[row]);
      }
    }
    
#ifdef DEBUG_ELIMINATION
    cout << "Matrix is now:\n";
    dumpMatrix(matrix, places, trans, places);
#endif
    row++;
  } // for col


  for (unsigned r=0; r<places; r++) {
    normalizeRow(matrix[r], places+trans);
  }
#ifdef DEBUG_ELIMINATION
  cout << "Final matrix:\n";
  dumpMatrix(matrix, places, trans, places);
#endif
}



/* ============================================================ */

unsigned firstnz(const int* v, unsigned n)
{
  for (unsigned i=0; i<n; i++) {
    if (v[i]) return i;
  }
  return n;
}


bool belongsToVectorSpace(
  int* vector, 
  const int* const* basis, 
  unsigned numrows, 
  unsigned numcols)

{
#ifdef DEBUG_BELONGSTO
  cout << "Checking if vector\n";
  showRow(cout, vector, numrows, numcols - numrows);
  cout << "belongs to vector space with basis\n";
  for (unsigned i=0; i<numrows; i++) {
    showRow(cout, basis[i], numrows, numcols - numrows);
  }
#endif
  unsigned r = 0;
  for (unsigned c=0; c<numcols; c++) {
    if (0==vector[c]) continue;

    // need to zero out vector[c].
    // find a basis vector whose first nonzero element is c.
    // If there isn't one, then the vector is linearly dependent.
    
    for (; r<numrows; r++) {
      unsigned nz = firstnz(basis[r], numcols);
      if (nz < c) continue;
      if (nz > c) {
#ifdef DEBUG_BELONGSTO
        cout << "Impossible to cancel element " << c << "\n";
#endif
        return false; 
      }
      break;
    }
    if (r >= numrows) {
#ifdef DEBUG_BELONGSTO
      cout << "Impossible to cancel element " << c << "\n";
#endif
      return false;
    }

#ifdef DEBUG_BELONGSTO
    cout << "Canceling element " << c << " with basis vector " << r << "\n";
#endif
    cancelByRow(c, numcols, vector, basis[r]);
#ifdef DEBUG_BELONGSTO
    cout << "Vector is now:\n";
    showRow(cout, vector, numrows, numcols - numrows);
#endif
    r++;

  } // for c
  return true;
}

