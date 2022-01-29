
EXES= chem_flows 

COMSRC= lexer.cc parser.cc gauss.cc eqn_util.cc
ALLSRC= chem_flows.cc $(COMSRC)

COMOBJ= $(COMSRC:.cc=.o)
ALLOBJ= $(ALLSRC:.cc=.o)

all: $(EXES)

# CXXFLAGS= -Wall -ggdb -std=c++11
CXXFLAGS= -Wall -O3 -std=c++11

%.o: %.cc
	g++ $(CXXFLAGS) -c $<

lextest: lextest.o lexer.o
	g++ -o lextest lextest.o lexer.o

chem_flows: chem_flows.o $(COMOBJ)
	g++ -o chem_flows chem_flows.o $(COMOBJ)

clean:
	rm $(EXES) $(ALLOBJ)

depend:
	makedepend -DSKIP_SYSTEM_INCLUDES $(ALLSRC)

# DO NOT DELETE

chem_flows.o: lexer.h parser.h eqn_util.h gauss.h
lexer.o: lexer.h
parser.o: parser.h lexer.h
gauss.o: gauss.h
eqn_util.o: eqn_util.h
