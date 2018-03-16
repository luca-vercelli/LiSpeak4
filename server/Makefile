
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
servicedir=/etc/init.d
DESTDIR=

#if user is not root, should run with: 
#make install prefix=~/.local exec_prefix=~
#However not everything will work

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
	mkdir -p $(DESTDIR)$(servicedir)

install: mkinstalldirs
	./setup.py install --prefix=$(prefix)
	#defaults to $(prefix)/lib/python2.7/dist-packages/ or site-packages 
	install -m=755 lispeak-server.py $(DESTDIR)$(bindir)/lispeak
	install -m=755 lispeak-service.sh $(DESTDIR)$(servicedir)/lispeak 

uninstall:
	rm -rf $(DESTDIR)$(bindir)/lispeak
	rm -rf $(DESTDIR)$(prefix)/lib/python2.7/site-packages/lispeak
	rm -rf $(DESTDIR)$(prefix)/lib/python2.7/dist-packages/lispeak
	rm -rf $(DESTDIR)$(servicedir)/lispeak

