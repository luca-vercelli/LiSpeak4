
#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
DESTDIR=

JARNAME=speech2text-0.1.jar
JARLINK=speech2text.jar

#AFAIK, we have 2 possibilities to run a JAR:
#(1) create a script that simply contains "java -jar myfile.jar"
#(2) let Linux to know how to open jar's

all:
	mvn package

mkinstalldirs:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(datarootdir)/java

install: mkinstalldirs
	#in Debian, use mh instead
	install -m 775 target/$(JARNAME) $(DESTDIR)$(datarootdir)/java
	ln -s $(DESTDIR)$(datarootdir)/java/$(JARNAME) $(DESTDIR)$(datarootdir)/java/$(JARLINK)
	install -m 775 src/main/sh/lispeak-start.sh $(DESTDIR)$(bindir)/lispeak-start
	install -m 775 src/main/sh/lispeak-start.sh $(DESTDIR)$(bindir)/lispeak-stop

uninstall:
	rm -rf $(DESTDIR)$(bindir)/lispeak-start
	rm -rf $(DESTDIR)$(bindir)/lispeak-stop
	rm -rf $(DESTDIR)$(datarootdir)/java/$(JARLINK)
	rm -rf $(DESTDIR)$(datarootdir)/java/$(JARNAME)

clean:
	mvn clean

