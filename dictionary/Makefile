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

mkinstalldirs:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(mandir)/man1
	mkdir -p $(DESTDIR)$(datarootdir)/gtksourceview-2.0/language-specs/
	mkdir -p $(DESTDIR)$(datarootdir)/gtksourceview-3.0/language-specs/
	mkdir -p $(DESTDIR)$(datarootdir)/lispeak

install: mkinstalldirs
	cp $(EXECUTABLE) $(DESTDIR)$(bindir)
	cp manpages/$(EXECUTABLE) $(DESTDIR)$(mandir)/man1/$(EXECUTABLE).1
	gzip $(DESTDIR)$(mandir)/man1/$(EXECUTABLE).1
	cp lidic.lang $(DESTDIR)$(datarootdir)/gtksourceview-2.0/language-specs/
	cp lidic.lang $(DESTDIR)$(datarootdir)/gtksourceview-3.0/language-specs/
	cp -r modes $(DESTDIR)$(datarootdir)/lispeak/

uninstall:
	rm -rf $(DESTDIR)$(datarootdir)/modes
	rm -rf $(DESTDIR)$(datarootdir)/gtksourceview-2.0/language-specs/lidic.lang
	rm -rf $(DESTDIR)$(datarootdir)/gtksourceview-3.0/language-specs/lidic.lang
	rm -rf $(DESTDIR)$(mandir)/man1/$(EXECUTABLE).1.gz
	rm -rf $(DESTDIR)$(bindir)/$(EXECUTABLE)

clean:
	rm -rf $(EXECUTABLE)

