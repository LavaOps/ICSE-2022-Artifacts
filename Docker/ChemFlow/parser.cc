
#include "parser.h"

#include <stdarg.h>
#include <string.h>

// #define DEBUG_PARSER
// #define DEBUG_SPECIES

using namespace std;

void parse_debug(const char* format, ...)
{
#ifdef DEBUG_PARSER
  va_list args;
  va_start(args, format);
  vfprintf(stderr, format, args);
  va_end(args);
#endif
}

parser::
parser(lexer &_L, unordered_map<string, unsigned> &_S, vector<string> &_R) :
  L(_L), Species(_S), Reactions(_R)
{
  A = 0;
}

void parser::startError() const
{
  fprintf(stderr, "ERROR (parser) file %s line %u text %s:\n",
    L.Filename(),
    L.Lineno(),
    L.next_text()
  );
}

bool parser::expectingError(tokentype T) const
{
  startError();
  fprintf(stderr, "\tExpecting ");
  tokenName(stderr, T);
  fputc('\n', stderr);
  exit(1);
  return false;
}

bool parser::expectingError(tokentype T1, tokentype T2) const
{
  startError();
  fprintf(stderr, "\tExpecting ");
  tokenName(stderr, T1);
  fprintf(stderr, " or ");
  tokenName(stderr, T2);
  fputc('\n', stderr);
  exit(1);
  return false;
}

unsigned parser::get_species_index(const char* c)
{
  string s(c);

  if (Species.count(s)) {
#ifdef DEBUG_SPECIES
    fprintf(stderr, "Species %s has index %u\n", c, Species[s]);
#endif
    return Species[s];
  }
  unsigned sz = Species.size();
#ifdef DEBUG_SPECIES
  fprintf(stderr, "Adding Species %s with index %u\n", c, sz);
#endif
  Species[s] = sz;
  return sz;
}

bool parser::parse_reaction(unsigned t)
{
  /* Before -> */ 
  parse_debug("Parsing reaction LHS in %s near line %u:\n",
    L.Filename(), L.Lineno()
  );

  if (END == L.next_token()) return false;

  int cardinality;
  unsigned p;

  //
  // Reaction is of the form
  //
  // [ IDENT : ]  [ INTEGER ] IDENT + ... + [ INTEGER ] IDENT ->
  //              [ INTEGER ] IDENT + ... + [ INTEGER ] IDENT ;
  //
  // where [] indicates 'optional'.
  //


  //
  // If the first symbol is IDENT, check for :
  // 

  if (IDENT == L.next_token()) {
    char ident[128];
    strncpy(ident, L.next_text(), 128);

    L.consume_token();
    if (':' == L.next_token()) {
      // Label.
      L.consume_token();
      if (t < Reactions.size()) {
        Reactions[t] = ident;
      }
      parse_debug("Got reaction label %s\n", ident);

      // IDENT : • [ INTEGER ] IDENT + ...

    } else {
      // Species with cardinality 1.
      p = get_species_index(ident);
      if (A) A[p].add_elem(t, -1);
      parse_debug("Got species %s\n", ident);

      if ('+' == L.next_token()) {
        // OK
        L.consume_token();
        //  IDENT + • [ INTEGER ] IDENT + ...
      } else {
        if (ARROW != L.next_token()) {
          expectingError(ARROW);
          return false;
        }
        // IDENT • ->
      }
    }
  }

  //
  // Read until ->
  //
  // Each time, it will be: optional integer, ident, + or ->
  //
  if (ARROW == L.next_token()) {
    L.consume_token();
  } else for (;;) {

    // Optional cardinality
    if (INTEGER == L.next_token()) {
      cardinality = L.next_value();
      L.consume_token();
    } else {
      cardinality = 1;
    }
    
    // Required identifier
    if (IDENT != L.next_token()) {
      expectingError(IDENT);
      return false;
    }
    
    parse_debug("Got next reactant %d %s\n", cardinality, L.next_text());
    
    p = get_species_index(L.next_text());
    if (A) A[p].add_elem(t, -cardinality);

    L.consume_token();

    // Keep going on +, stop on ->, error otherwise

    if ('+' == L.next_token()) {
      L.consume_token();
      continue;
    } 

    if (ARROW == L.next_token()) {
      L.consume_token();
      break;
    }

    expectingError(PLUS, ARROW);
    return false;
  } // else for

  /* After -> */
  parse_debug("Parsing reaction RHS in %s near line %u:\n",
    L.Filename(), L.Lineno()
  );

  //
  // Read until ;
  //
  if (';' == L.next_token()) {
    L.consume_token();
  } else for (;;) {
    
    // Optional cardinality
    if (INTEGER == L.next_token()) {
      cardinality = L.next_value();
      L.consume_token();
    } else {
      cardinality = 1;
    }
    
    // Required identifier
    if (IDENT != L.next_token()) {
      expectingError(IDENT);
      return false;
    }
    
    parse_debug("Got next reactant %d %s\n", cardinality, L.next_text());
    
    p = get_species_index(L.next_text());
    if (A) A[p].add_elem(t, cardinality);

    L.consume_token();

    // Keep going on +, stop on ;, error otherwise

    if ('+' == L.next_token()) {
      L.consume_token();
      continue;
    } 

    if (';' == L.next_token()) {
      L.consume_token();
      break;
    }

    expectingError(PLUS, SEMI);
    return false;
  }

  parse_debug("Done parsing reaction\n");
  return true;
}

