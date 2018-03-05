
#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
DESTDIR=

#TODO
#if user is not root, should switch to 
#bindir=~/bin
#datarootdir=~/.local/share

install:
	cp lispeak-settings.py $(DESTDIR)$(bindir)/lispeak-settings
	cp settings.glade $(DESTDIR)$(datarootdir)/lispeak/glade
	cp mic.png $(DESTDIR)$(datarootdir)/lispeak/glade

