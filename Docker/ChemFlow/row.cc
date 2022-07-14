
#include "row.h"

#include <cstdlib>
#include <climits>

template <class T>
inline T ABS(T a)
{
  return (a<0) ? -a : a;
}

template <class T>
inline int SIGN(T a)
{
	return (a >= 0) ? 1 : -1;
}

inline void ABORT(const char* msg)
{
	std::cerr << msg << "\n";
	exit(1);
}

template <class T, class U>
inline void safe_plusequal(T& a, U b)
{
	if (a>=0) {
		if (b>=0) {
			a += b;
			if (a<0) ABORT("Integer overflow on addition");
		} else {
			a += b;
		}
	} else { // a is negative
		if (b<0) {
      a += b;
			if (a>0) ABORT("Integer overflow on addition");
		} else {
			a += b;
		}
	}
}

row::row()
{
	elems = 0;
	width = 0;
}

row::~row()
{
	delete[] elems;
}

void row::clear()
{
	for (unsigned i=0; i<width; i++) {
		elems[i] = 0;
	}
}

void row::swap(row &r)
{
	if (elems == r.elems) return;

#ifdef USE_LONGS
	long* te = r.elems;
#else
	int* te = r.elems;
#endif
	unsigned tw = r.width;
	r.elems = elems;
	r.width = width;
	elems = te;
	width = tw;
}

void row::set_width(unsigned w)
{
	delete[] elems;
#ifdef USE_LONGS
	elems = new long[w];
#else
	elems = new int[w];
#endif
	width = w;
	for (unsigned i=0; i<width; i++) {
		elems[i] = 0;
	}
}

void row::zeroElem(unsigned i, const row& r)
{
	if (i>= width) return;
	if (0==elems[i]) return;
	if (0==r[i]) return;

	const long L = lcm(elems[i], r[i]);
	const long a = SIGN(-r[i]) * L / ABS(elems[i]);
	const long b = SIGN(elems[i]) * L / ABS(r[i]);

	check_multiply(a);
	r.check_multiply(b);

  for (unsigned i=0; i<width; i++) {
		elems[i] *= a;
		safe_plusequal(elems[i], b*r[i]);
  }

	normalize();
}

void row::normalize()
{
	int g = 0;
	int gs = 1;
	for (unsigned i=0; i<width; i++) {
		if (elems[i]) {
			if (g)	{
				g = gcd(g, ABS(elems[i]));
			}
			else {
				if (elems[i] > 0) {
					g = elems[i];
				} else {
					g = -elems[i];
					gs = -1;
				}
			}
		}
	}
	g *= gs;
	if (0==g) return;
	if (1==g) return;
	for (unsigned i=0; i<width; i++) {
		elems[i] /= g;
	}
}

bool row::visit_nonzeroes(visitor &v) const
{
	for (unsigned i=0; i<width; i++) {
		if (elems[i]) {
			if (v.visit(i, elems[i])) return true;
		}
	}
	return false;
}

void row::dump_full(std::ostream &out) const
{
	out << "[ ";
	for (unsigned i=0; i<width; i++) {
		out << elems[i] << " ";
	}
	out << "]";
}

void row::dump_sparse(std::ostream &out) const
{
	out << "[ ";
	for (unsigned i=0; i<width; i++) {
		if (elems[i]) {
			out << i << ":" << elems[i] << " ";
		}
	}
	out << "]";
}

void row::check_multiply(long a) const
{
	if (0==a) return;

	// Any elements larger than maxval in magnitude
	// will overflow when multiplied.
	
#ifdef USE_LONGS
	const long maxval = LONG_MAX / ABS(a);
#else
	const long maxval = INT_MAX / ABS(a);
#endif
	
	for (unsigned i=0; i<width; i++) {
		if (ABS(elems[i]) > maxval) {
			ABORT("integer overflow on multiply");
		}
	}
}

long row::gcd(long a, long b)
{
  while (b) {
    long t = b;
    b = a % b;
    a = t;
  }
  return a;
}

long row::lcm(long a, long b)
{
  a = ABS(a);
  b = ABS(b);
  return (a*b) / gcd(a,b);
}



