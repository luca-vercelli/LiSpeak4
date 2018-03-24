DIRS=it

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
#not sure if everything will work


all:
	-for d in $(DIRS); do (sphinx_lm_convert -i $dd/model.lm -o model.lm.bin ); done

mkinstalldirs:
	-for d in $(DIRS); do (mkdir -p $(DESTDIR)$(datarootdir)/sphinx-lispeak-$dd); done

install:
	-for d in $(DIRS); do (cp $dd/model.lm.bin $(DESTDIR)$(datarootdir)/sphinx-lispeak-$dd) ; done

uninstall:
	-for d in $(DIRS); do (rm -rf $(DESTDIR)$(datarootdir)/sphinx-lispeak-$dd) ; done

clean :
	-for d in $(DIRS); do (cd $$d; rm model.lm.bin ); done

