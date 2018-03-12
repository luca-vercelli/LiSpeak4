
#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
DESTDIR=

#if user is not root, should run with: 
#make install prefix=~/.local exec_prefix=~

all:
	#nothing to do

clean:
	#nothing to do

mkinstalldirs:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(datarootdir)/lispeak
	mkdir -p $(DESTDIR)$(datarootdir)/python2.7
	mkdir -p $(DESTDIR)/var/run/lispeak

install: mkinstalldirs
	cp lispeak-server.py $(DESTDIR)$(bindir)/lispeak-server
	cp -r lispeak $(DESTDIR)$(datarootdir)/python2.7

uninstall:
	rm -rf $(DESTDIR)$(bindir)/lispeak-server
	rm -rf $(DESTDIR)$(datarootdir)/python2.7/lispeak

