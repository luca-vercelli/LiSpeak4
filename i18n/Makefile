LANGUAGES=it

#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
libdir=$(exec_prefix)/lib
localstatedir=/var
runstatedir=$(localstatedir)/run
DESTDIR=

#if user is not root, should run with: 
#make install prefix=~/.local exec_prefix=~
#not sure if everything will work


all:
	for l in $(LANGUAGES); do  msgfmt $$l.po -o $$l.mo ; done

mkinstalldirs:
	for l in $(LANGUAGES); do  (mkdir -p $(DESTDIR)$(datarootdir)/locale/$$l/LC_MESSAGES ) ; done

install: mkinstalldirs
	for l in $(LANGUAGES); do  (cp $$l.mo $(DESTDIR)$(datarootdir)/locale/$$l/LC_MESSAGES/lispeak.mo ) ; done

uninstall:
	for l in $(LANGUAGES); do  (rm -f $(DESTDIR)$(datarootdir)/locale/$$l/LC_MESSAGES/lispeak.mo ) ; done

clean:
	rm -f *.mo

