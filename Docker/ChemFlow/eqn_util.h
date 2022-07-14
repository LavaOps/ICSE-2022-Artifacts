
#ifndef EQN_UTIL_H
#define EQN_UTIL_H

#include <string>
#include <vector>
#include "row.h"

enum class eqtype {
  EMPTY,      // empty row
  FLOW,       // proper flow (all 0 transition coefficients)
  INEQUALITY, // all transition coefficients have the same sign
  USELESS     // some transition coefficients have different signs
};


/*
  Determine equation type based on transition coefficients.
*/
eqtype invariantType(const row& r, unsigned trans, unsigned places);

/*
  Display an equation
*/
void showRow(const row& r, 
  const std::vector<const char*> &placename,
  const std::vector<std::string> &transname);


#endif

