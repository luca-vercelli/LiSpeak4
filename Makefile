DIRS=settings dictionary speech2text

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

