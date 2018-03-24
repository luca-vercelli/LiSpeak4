DIRS=dictionary speech2text server settings i18n

#if user is not root, should run with: 
#make install prefix=~/.local exec_prefix=~
#not sure if everything will work


all:
	-for d in $(DIRS); do (cd $$d; $(MAKE) $@ ); done

mkinstalldirs:
	-for d in $(DIRS); do (cd $$d; $(MAKE) $@ ); done

install:
	-for d in $(DIRS); do (cd $$d; $(MAKE) $@ ); done

uninstall:
	-for d in $(DIRS); do (cd $$d; $(MAKE) $@ ); done

clean :
	-for d in $(DIRS); do (cd $$d; $(MAKE) $@ ); done

