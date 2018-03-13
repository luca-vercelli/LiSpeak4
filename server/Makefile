
#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
libdir=$(exec_prefix)/lib
localstatedir=$(prefix)/var
runstatedir=$(localstatedir)/run
DESTDIR=

#if user is not root, should run with: 
#make install prefix=~/.local exec_prefix=~

all:
	./setup.py build

clean:
	rm -rf build

mkinstalldirs:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(datarootdir)/lispeak
	mkdir -p $(DESTDIR)$(libdir)/python2.7
	mkdir -p $(DESTDIR)$(runstatedir)/lispeak
	chmod 775 $(DESTDIR)$(runstatedir)/lispeak

install: mkinstalldirs
	./setup.py install
	#defaults to /usr/local/lib/python2.7/dist-packages/
	cp lispeak-server.py $(DESTDIR)$(bindir)/lispeak-server
	cp lispeak-service.sh $(DESTDIR)$(bindir)/etc/init.d
	cp -r lispeak $(DESTDIR)$(libdir)/python2.7

uninstall:
	rm -rf $(DESTDIR)$(bindir)/lispeak-server
	rm -rf $(DESTDIR)$(libdir)/python2.7/lispeak

