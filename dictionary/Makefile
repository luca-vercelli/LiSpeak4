CC=gcc
CFLAGS=-c -Wall -Wno-unused  
#LDFLAGS=-O3    #with this line, we get a Segmentation fault
SOURCES=src/dictionary.c src/match.c src/commands.c
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=dictionary

#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
DESTDIR=


all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@
.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
check-syntax:
	$(CC) $(CFLAGS) -fsyntax-only $(SOURCES)

install:
	cp $(EXECUTABLE) $(DESTDIR)$(bindir)
	cp manpages/$(EXECUTABLE) $(DESTDIR)$(mandir)
	cp lidic.lang $(DESTDIR)$(datarootdir)/gtksourceview-2.0/language-specs/
	cp lidic.lang $(DESTDIR)$(datarootdir)/gtksourceview-3.0/language-specs/
	