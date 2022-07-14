
#include <iostream>
#include "gauss.h"
#include <assert.h>

// #define DEBUG_ELIMINATION
// #define DUMP_FULL
// #define DEBUG_BELONGSTO

// #define OLD_CANCEL

template <class T>
inline T ABS(T a)
{
  return (a<0) ? -a : a;
}


/* 
 * NEW STUFF HERE
 */

/* ============================================================ */

/*
  Gaussian Elimination
*/

void matrixElim(row* matrix, unsigned nrows, unsigned ncols)
{
#ifdef DEBUG_ELIMINATION
  cout << "Starting Gaussian Elimination on matrix:\n";
	for (unsigned i=0; i<nrows; i++) {
		cout << "Row " << i << " ";
#ifdef DUMP_FULL
		matrix[i].dump_full(cout);
#else
		matrix[i].dump_sparse(cout);
#endif
		cout << "\n";
	}
#endif

  unsigned c; // column to eliminate
  unsigned r = 0; // row we're using to eliminate
  for (c=0; c<ncols; c++) {
    if (r >= nrows) break;

    //  Find 'best' row to eliminate this column:
    //    smallest magnitude, non-zero integer coefficient.
    unsigned bestrow = nrows;    // invalid row
    for (unsigned i = r; i<nrows; i++) {
      if (0==matrix[i][c]) continue;
      if (bestrow >= nrows) {
        bestrow = i;
        continue;
      }
      // see which is better
      if ( ABS(matrix[bestrow][c]) > ABS(matrix[i][c]) ) {
        bestrow = i;
      }
    } // for r

    // If no non-zero rows, then the column is already eliminated.
    // Go to the next column in that case.
    if (bestrow >= nrows) continue;

#ifdef DEBUG_ELIMINATION
    cout << "Using row " << bestrow << " to zero out column " << c << "\n"; 
#endif

    // Put the best row 'first' by swapping rows
		matrix[r].swap(matrix[bestrow]);

    // Cancel all other rows by this row
    for (unsigned i = 0; i<nrows; i++) { 
      if (i != r) {
				matrix[i].zeroElem(c, matrix[r]);
      }
    }
    
#ifdef DEBUG_ELIMINATION
    cout << "Matrix is now:\n";
		for (unsigned i=0; i<nrows; i++) {
			cout << "Row " << i << " ";
#ifdef DUMP_FULL
			matrix[i].dump_full(cout);
#else
			matrix[i].dump_sparse(cout);
#endif
			cout << "\n";
		}
#endif
    r++;
  } // for c

  for (unsigned i=0; i<nrows; i++) { 
		matrix[i].normalize();
  }
#ifdef DEBUG_ELIMINATION
  cout << "Final matrix:\n";
	for (unsigned i=0; i<nrows; i++) {
		cout << "Row " << i << " ";
#ifdef DUMP_FULL
	  matrix[i].dump_full(cout);
#else
		matrix[i].dump_sparse(cout);
#endif
		cout << "\n";
	}
#endif
}

/* ============================================================ */

bool belongsToVectorSpace(
  row& vector, 
  const row* basis,
  unsigned numrows, 
  unsigned numcols)

{
#ifdef DEBUG_BELONGSTO
  cout << "Checking if vector\n";
	vector.dump_full(cout);
	cout << "\nbelongs to vector space with basis\n";
  for (unsigned i=0; i<numrows; i++) {
		basis[i].dump_full(cout);
		cout << "\n";
  }
#endif
  unsigned r = 0;
  for (unsigned c=0; c<numcols; c++) {
    if (0==vector[c]) continue;

    // need to zero out vector[c].
    // find a basis vector whose first nonzero element is c.
    // If there isn't one, then the vector is linearly dependent.
    
    for (; r<numrows; r++) {
      unsigned nz = basis[r].first_nonzero();
			if (0==nz) continue;	// shouldn't happen!
			--nz;
      if (nz < c) continue;
      if (nz > c) continue;
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
		vector.zeroElem(c, basis[r]);
#ifdef DEBUG_BELONGSTO
    cout << "Vector is now:\n";
		vector.dump_full(cout);
		cout << "\n";
#endif
    r++;

  } // for c
  return true;
}

