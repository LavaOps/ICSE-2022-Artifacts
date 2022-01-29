
#ifndef LEXER_H
#define LEXER_H

#include <stdio.h>

enum tokentype {
    END     = 0,
    SEMI    = ';',
    PLUS    = '+',
    COLON   = ':',

    INTEGER   = 300,
    IDENT     = 301,
    ARROW     = 302
};

inline void tokenName(FILE* fout, tokentype T)
{
  switch (T) {
    case END:       fprintf(fout, "EOF");             return;
    case SEMI:      fprintf(fout, ";");               return;
    case PLUS:      fprintf(fout, "+");               return;
    case COLON:     fprintf(fout, ":");               return;
    case INTEGER:   fprintf(fout, "integer");         return;
    case IDENT:     fprintf(fout, "identifier");      return;
    case ARROW:     fprintf(fout, "->");              return;
    default:        fprintf(fout, "?unknown token?");
  }
}

static const unsigned MAX_IDENT = 64; 

class lexer {
    char* inbuf;
    char* ptr;
    FILE* infile;

    const char* filename;
    const char* basename;
    unsigned lineno;

    tokentype token;
    char lexeme[MAX_IDENT+1];
    long integer;

  public:
    lexer(const char* fn);
    ~lexer();

    inline operator bool() const {
      return infile;
    }
    inline const char* Filename() const {
      return filename;
    }
    inline const char* Basename() const {
      return basename;
    }
    inline unsigned Lineno() const {
      return lineno;
    }

    inline tokentype    next_token()  const { return token; }
    inline long         next_value()  const { return integer; }
    inline const char*  next_text()   const { return lexeme; }

    void consume_token();

    inline void restart() {
      if (infile) {
        rewind(infile);
        refill();
        token = END;
        integer = 0;
        consume_token();
      }
    }

  private:
    inline bool eof() const { return 0==ptr; }
    inline char peek() const { return *ptr; }
    inline void nextc() {
        if (0==*(++ptr)) refill();
    }
    inline char getc() {
      char c = *ptr;
      nextc();
      return c;
    }
    void refill();

    void consume_ident();
    void consume_number();

  private:  // Keep Jim happy
    lexer(const lexer &L) = delete;
    lexer& operator=(const lexer &L) = delete;
};

#endif

