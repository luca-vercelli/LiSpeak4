
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
	mkdir -p $(DESTDIR)$(datarootdir)/lispeak/glade

install: mkinstalldirs
	cp lispeak-settings.py $(DESTDIR)$(bindir)/lispeak-settings
	cp settings.glade $(DESTDIR)$(datarootdir)/lispeak/glade
	cp mic.png $(DESTDIR)$(datarootdir)/lispeak/glade

uninstall:
	rm -rf $(DESTDIR)$(datarootdir)/lispeak/glade
	rm -rf $(DESTDIR)$(bindir)/lispeak-settings

