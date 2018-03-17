
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
	./setup.py build

clean:
	rm -rf build
	rm -rf lispeak/*.pyc
	rm -rf lispeak/make_conf.py

mkinstalldirs:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(datarootdir)/lispeak

install: mkinstalldirs
	# We rebuild the package in order to create make_conf.py. Any other way?
	echo > lispeak/make_conf.py  
	echo "prefix='$(prefix)'" >> lispeak/make_conf.py  
	echo "bindir='$(bindir)'" >> lispeak/make_conf.py  
	echo "datarootdir='$(datarootdir)'" >> lispeak/make_conf.py  
	./setup.py build
	# Here starts the real install
	./setup.py install --prefix=$(prefix)
	# defaults to $(prefix)/lib/python2.7/dist-packages/ or site-packages 
	install -m=755 lispeak-server.py $(DESTDIR)$(bindir)/lispeak

uninstall:
	rm -rf $(DESTDIR)$(bindir)/lispeak
	#hope to find correct path 
	rm -rf $(DESTDIR)$(prefix)/lib/python2.7/site-packages/lispeak
	rm -rf $(DESTDIR)$(prefix)/lib/python2.7/dist-packages/lispeak

