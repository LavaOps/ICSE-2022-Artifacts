
#include "lexer.h"
#include "parser.h"
#include "eqn_util.h"
#include "gauss.h"

using namespace std;


int main(int argc, const char** argv)
{
  if (argc != 2) {
    fprintf(stderr, "Usage: %s infile\n\n", argv[0]);
    return 1;
  }

  lexer L(argv[1]);

  if (!L) {
    fprintf(stderr, "Couldn't read from file %s\n", argv[1]);
    exit(1);
  }

  unordered_map<string, unsigned> Species;
  vector<string> Reactions;
  vector<const char*> index2species;

  parser P(L, Species, Reactions);

  fprintf(stderr, "Reading from %s\nPass 1\n", argv[1]);

  const unsigned trans = P.parse_file();
  const unsigned places = Species.size();

  fprintf(stderr, "There are:\n\t%u species\n\t%u reactions\n", places, trans);

  /* Allocate stuff here */

  index2species.resize(places);
  unsigned i;
  unordered_map<string, unsigned>::iterator it;
  for (i=0; i<places; i++) index2species[i] = 0;
  for (it = Species.begin(); it != Species.end(); ++it) {
    index2species[it->second] = it->first.c_str();
  }

  // Set default reaction names
  Reactions.resize(trans);
  for (i=0; i<trans; i++) {
    stringstream thing;
    thing << "(reaction " << i+1 << ")";
    Reactions[i] = thing.str();
  }

#ifdef DEBUG_SPECIES 
  for (i=0; i<=places; i++) {
    if (index2species[i]) 
      cout << "species " << i << " : " << index2species[i] << "\n";
  }
#endif

  int** matrix;
  // there are P rows
  // each row is a vector of the form
  // [ #trans | #places ]
  matrix = new int* [places];
  for (i=0; i<places; i++) {
    matrix[i] = new int[places + trans];
    for (int j=places+trans-1; j>=0; j--) {
      matrix[i][j] = 0;
    }
    matrix[i][trans+i] = -1;
  }

  fprintf(stderr, "Pass 2\n");
  L.restart();
  P.set_matrix(matrix);

  P.parse_file();

  matrixElimStd(matrix, trans, places);

  printf("Flows (== constant):\n");
  for (i=0; i<places; i++) 
    if (eqtype::FLOW == invariantType(matrix[i], trans, places)) 
    {
      fputc('\t', stdout);
      showRow(matrix[i], index2species, Reactions);
    }

  printf("\nInequalities (remove reactions, <= constant):\n");
  for (i=0; i<places; i++) 
    if (eqtype::INEQUALITY == invariantType(matrix[i], trans, places)) 
    {
      fputc('\t', stdout);
      showRow(matrix[i], index2species, Reactions);
    }

  printf("\nIrreducible:\n");
  for (i=0; i<places; i++) 
    if (eqtype::USELESS == invariantType(matrix[i], trans, places)) 
    {
      fputc('\t', stdout);
      showRow(matrix[i], index2species, Reactions);
    }


  return 0;
}

