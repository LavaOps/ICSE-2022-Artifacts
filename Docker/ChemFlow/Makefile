
EXES= chem_flows

COMSRC= lexer.cc parser.cc gauss.cc eqn_util.cc row.cc

COMOBJ= $(COMSRC:.cc=.o)

all: $(EXES)

# CXXFLAGS= -Wall -ggdb -std=c++11
CXXFLAGS= -Wall -O3 -std=c++11

%.o: %.cc
	g++ $(CXXFLAGS) -c $<

chem_flows: chem_flows.o $(COMOBJ)
	g++ -o $@ $^

clean:
	rm $(EXES) $(ALLOBJ)

depend:
	makedepend -DSKIP_SYSTEM_INCLUDES $(COMSRC)

# DO NOT DELETE

crn_flows.o: lexer.h parser.h row.h eqn_util.h gauss.h
lexer.o: lexer.h
parser.o: parser.h lexer.h row.h
gauss.o: gauss.h row.h
eqn_util.o: eqn_util.h row.h
row.o: row.h
