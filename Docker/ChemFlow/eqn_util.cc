
#include "eqn_util.h"

// #define FANCY_OUT

eqtype invariantType(const int* row, unsigned trans, unsigned places)
{
  int sign = 0;
  for (unsigned i=0; i<trans; i++) {
    if (0==row[i]) continue;
    int rsign = (row[i] > 0) ? 1 : -1;
    if (0==sign) {
      sign = rsign;
    } else {
      if (sign != rsign) return eqtype::USELESS;
    }
  }
  if (sign) return eqtype::INEQUALITY;
  for (unsigned i=trans; i<trans+places; i++) {
    if (row[i]) return eqtype::FLOW;
  }
  return eqtype::EMPTY;
}


inline void showWeight(bool printed, int wt)
{
  if (wt < 0) {
#ifdef FANCY_OUT
    fputc('-', stdout);
    if (printed) fputc(' ', stdout);
    if (wt < -1) printf("%d", -wt);
#else
    printf("%d ", wt);
#endif
  } else {
#ifdef FANCY_OUT
    if (printed) fputs("+ ", stdout);
    if (wt > 1)  printf("%d", wt);
#else
    printf("+%d ", wt);
#endif
  }
}


void showRow(const int* row, 
  const std::vector<const char*> &placename,
  const std::vector<std::string> &transname)
{
  if (0==row) return;
  bool printed = false;
  unsigned i;
  const unsigned places = placename.size();
  const unsigned trans = transname.size();
  for (i=0; i<trans; i++) {
    if (0==row[i]) continue;
    showWeight(printed, row[i]);
#ifdef INDEX_OUT
    printf(" r%u", i);
#else
    fputs(transname[i].c_str(), stdout);
#endif
    fputc(' ', stdout);
    printed = true;
  }
  for (; i<places+trans; i++) {
    if (0==row[i]) continue;
    showWeight(printed, row[i]);
#ifdef INDEX_OUT
    printf(" s%u", i-trans);
#else
    fputs(placename[i-trans], stdout);
#endif
    fputc(' ', stdout);
    printed = true;
  }
  fputc('\n', stdout);
}

