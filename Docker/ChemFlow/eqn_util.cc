
#include "eqn_util.h"

// #define FANCY_OUT

eqtype invariantType(const row& r, unsigned trans, unsigned places)
{
  int sign = 0;
  for (unsigned i=0; i<trans; i++) {
    if (0==r[i]) continue;
    int rsign = (r[i] > 0) ? 1 : -1;
    if (0==sign) {
      sign = rsign;
    } else {
      if (sign != rsign) return eqtype::USELESS;
    }
  }
  if (sign) return eqtype::INEQUALITY;
  for (unsigned i=trans; i<trans+places; i++) {
    if (r[i]) return eqtype::FLOW;
  }
  return eqtype::EMPTY;
}


inline void showWeight(bool printed, long wt)
{
	using namespace std;
  if (wt < 0) {
#ifdef FANCY_OUT
		cout << "-";
    if (printed) cout << " ";
    if (wt < -1) cout << -wt;
#else
		cout << wt << " ";
#endif
  } else {
#ifdef FANCY_OUT
    if (printed) cout << "+ ";
    if (wt > 1)  cout << wt;
#else
		cout << "+" << wt << " ";
#endif
  }
}


void showRow(const row& r, 
  const std::vector<const char*> &placename,
  const std::vector<std::string> &transname)
{
  bool printed = false;
  unsigned i;
  const unsigned places = placename.size();
  const unsigned trans = transname.size();
  for (i=0; i<trans; i++) {
    if (0==r[i]) continue;
    showWeight(printed, r[i]);
#ifdef INDEX_OUT
    printf(" r%u", i);
#else
    fputs(transname[i].c_str(), stdout);
#endif
    fputc(' ', stdout);
    printed = true;
  }
  for (; i<places+trans; i++) {
    if (0==r[i]) continue;
    showWeight(printed, r[i]);
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

