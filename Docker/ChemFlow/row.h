#ifndef ROW_H
#define ROW_H

#include <iostream>

#define USE_LONGS

class row {
#ifdef USE_LONGS
		long* elems;
#else
		int* elems;
#endif
		unsigned width;
	public:
		class visitor {
			public:
					visitor() { }
					virtual ~visitor() { }
					virtual bool visit(unsigned elem, long value) = 0;
		};

	public:
		row();
		~row();

		void clear();

		void swap(row &r);

		void set_width(unsigned w);
		inline void add_elem(unsigned i, long v) {
			if (i<width) elems[i] += v;
		}

		inline unsigned first_nonzero() const {
			for (unsigned i=0; i<width; i++) if (elems[i]) return i+1;
			return 0;
		}

		inline long operator[] (unsigned i) const {
			return (i<width) ? elems[i] : 0;
		}

		void zeroElem(unsigned i, const row& r);

		void normalize();

		// Return true (and stop) if v.visit() returns true.
		bool visit_nonzeroes(visitor &v) const;

		void dump_full(std::ostream &out) const;
		void dump_sparse(std::ostream &out) const;

	protected:
		void check_multiply(long a) const;

		static long gcd(long a, long b);
		static long lcm(long a, long b);
};

#endif
