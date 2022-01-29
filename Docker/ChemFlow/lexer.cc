
#include "lexer.h"

#include <stdlib.h>

#define IGNORE_AFTER_SEMI

const unsigned BUFSIZE = 16384;

lexer::lexer(const char* fn)
{
  inbuf = 0;
  ptr = 0;
  filename = fn;
  lineno = 1;

  basename = fn;
  for (; *fn; fn++) {
    if ('/' == *fn) {
      basename = fn+1;
    }
  }

  infile = fopen(filename, "r");
  if (infile) {
    inbuf = new char[BUFSIZE+1];
    refill();
  }

  token = END;
  integer = 0;
  consume_token();
}

lexer::~lexer()
{
  if (infile) fclose(infile);
  delete[] inbuf;

}

void lexer::consume_token()
{
  for (;;) {
    if (eof()) {
      token = END;
      lexeme[0] = 0;
      integer = 0;
      return;
    }
    char c = getc();

    if (' ' == c) continue;
    if ('\t' == c) continue;
    if ('\r' == c) continue;
    if ('\n' == c) {
      lineno++;
      continue;
    }

    if ('#' == c) {
      // ignore until newline
      for (;;) {
        if (eof()) break;
        c = getc();
        if ('\n' == c) {
          lineno++;
          break;
        }
      }
      continue;
    }

    lexeme[0] = c;

    if ( ('+' == c) || (';' == c) || (':' == c) ) {
      lexeme[1] = 0;
      token = tokentype(c);
      integer = 0;
#ifdef IGNORE_AFTER_SEMI
      if (';' == c) {
        // ignore until newline
        for (;;) {
          if (eof()) break;
          c = getc();
          if ('\n' == c) {
            lineno++;
            return;
          }
        }
      }
#endif
      return;
    }

    if ('-' == c) {
      if ('>' == peek()) {
        nextc();
        lexeme[1] = '>';
        lexeme[2] = 0;
        integer = 0;
        token = ARROW;
        return;
      }
    }

    if (('a'<= c) && (c <= 'z')) {
      return consume_ident();
    }
    if (('A'<= c) && (c <= 'Z')) {
      return consume_ident();
    }
    if ('_' == c) {
      return consume_ident();
    }
    if (('0' <= c) && (c <= '9')) {
      return consume_number();
    }
    
    fprintf(stderr, "ERROR (lexer) file %s line %u:\n", filename, lineno);
    fprintf(stderr, "\tIgnoring unexpected character '%c'\n", c);
  }
}


void lexer::refill()
{
  if (infile) {
    size_t bytes = fread(inbuf, 1, BUFSIZE, infile);
    if (bytes) {
      inbuf[bytes] = 0;
      ptr = inbuf;
    } else {
      ptr = 0;
    }
  }
}

inline bool is_identifier_char(int c)
{
  if (('a' <= c) && (c <= 'z')) return true;
  if (('A' <= c) && (c <= 'Z')) return true;
  if (('0' <= c) && (c <= '9')) return true;
  return ('_' == c) || ('[' == c) || (']' == c);
}

void lexer::consume_ident()
{
  unsigned p;
  for (p = 1; ; p++) {
    if (eof()) break;
    char c = peek();
    if (is_identifier_char(c)) {
      if (p<MAX_IDENT) {
        lexeme[p] = c;
        nextc();
      }
      continue;
    }
    break;
  }
  if (p<=MAX_IDENT) {
    lexeme[p] = 0;
  } else {
    lexeme[MAX_IDENT] = 0;
  }
  integer = 0;
  token = IDENT;
}

void lexer::consume_number()
{
  unsigned p;
  for (p = 1; ; p++) {
    if (eof()) break;
    char c = peek();
    if (('0' <= c) && (c <= '9')) {
      if (p<MAX_IDENT) {
        lexeme[p] = c;
        nextc();
      }
      continue;
    }
    break;
  }
  if (p<=MAX_IDENT) {
    lexeme[p] = 0;
  } else {
    lexeme[MAX_IDENT] = 0;
  }
  integer = atol(lexeme);
  token = INTEGER;
}
