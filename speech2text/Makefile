
#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
DESTDIR=


make:
	mvn package

install:
	#in Debian, use mh instead
	cp target/*.jar $(DESTDIR)$(datarootdir)/java
	cp src/main/sh/* $(DESTDIR)$(bindir)
