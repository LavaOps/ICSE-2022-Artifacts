
void dumpMatrix(int** matrix, unsigned places, unsigned trans, unsigned supplement);

void matrixElimination(int** matrix, unsigned places, unsigned trans, unsigned& supplement);

/**
    Reduce a matrix using "standard" Gaussian elimination.
    @param  matrix  Matrix with integer coefficients,
                    as an array of row vectors.
                    Each row vector is of dimension \a trans + \a places.
                    There are \a places rows.

    @param  trans   Number of transitions / reactions
    @param  places  Number of places / species
*/
void matrixElimStd(int** matrix, unsigned trans, unsigned places);

/**
  Check if a given vector belongs to a vector space, given as a basis.
  In other words, checks if the vector is linearly dependent on the
  basis vectors, by attempting to zero out the vector.  On success,
  we know the vector is linearly dependent; otherwise, it is independent.
  
  @param  vector  The vector to check; will be modified.  
  @param  basis   The basis, as an array of vectors.
  @param  numrows Number of vectors in the basis
  @param  numcols Length of each vector in the basis, and the given vector.
                  
  @return true, if the input vector was successfully zeroed;
          false otherwise.
*/
bool belongsToVectorSpace(
  int* vector, 
  const int* const* basis, 
  unsigned numrows, 
  unsigned numcols);

