
#ifndef PARSER_H
#define PARSER_H

#include "lexer.h"

#include <vector>
#include <unordered_map>
#include <sstream>

class parser {
    lexer &L;

    std::unordered_map<std::string, unsigned> &Species;
    std::vector<std::string> &Reactions;

    int** A;

  public:
    parser( lexer &_L, 
            std::unordered_map<std::string, unsigned> &_S, 
            std::vector<std::string> &_R);

    inline void set_matrix(int** _A) {
      A = _A;
    }

    inline unsigned parse_file() {
      unsigned nr = 0;
      while (parse_reaction(nr++));
      return nr-1;
    }

  private:
    void startError() const;
    
    bool expectingError(tokentype T) const;
    bool expectingError(tokentype T1, tokentype T2) const;

    unsigned get_species_index(const char* c);

    bool parse_reaction(unsigned t);

  private:  // Keep Jim happy
    parser(const parser &P) = delete;
    parser& operator=(const parser &P) = delete;
};

#endif

