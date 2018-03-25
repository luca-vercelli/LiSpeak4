
#see https://www.gnu.org/prep/standards/html_node/Directory-Variables.html
prefix=/usr/local
exec_prefix=$(prefix)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
sysconfdir=$(prefix)/etc
mandir=$(datarootdir)/man
DESTDIR=

M2REPO=~/.m2/repository

JARNAME=speech2text-0.1.jar
JARLINK=speech2text.jar

LANGUAGES=it en

#AFAIK, we have 2 possibilities to run a JAR:
#(1) create a script that simply contains "java -jar myfile.jar"
#(2) let Linux to know how to open jar's

all:
	mvn package

mkinstalldirs:
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(datarootdir)/java

install: mkinstalldirs
	#
	#in Debian, use mh instead
	#
	install -m 775 target/$(JARNAME) $(DESTDIR)$(datarootdir)/java
	ln -sf $(DESTDIR)$(datarootdir)/java/$(JARNAME) $(DESTDIR)$(datarootdir)/java/$(JARLINK)
	#Dependencies
	install -m 775 $(M2REPO)/edu/cmu/sphinx/sphinx4-core/5prealpha-SNAPSHOT/sphinx4-core-5prealpha-SNAPSHOT.jar $(DESTDIR)$(datarootdir)/java
	ln -sf $(DESTDIR)$(datarootdir)/java/sphinx4-core-5prealpha-SNAPSHOT.jar $(DESTDIR)$(datarootdir)/java/sphinx4-core-5prealpha.jar
	install -m 775 $(M2REPO)/org/ini4j/ini4j/0.5.4/ini4j-0.5.4.jar $(DESTDIR)$(datarootdir)/java
	ln -sf $(DESTDIR)$(datarootdir)/java/ini4j-0.5.4.jar $(DESTDIR)$(datarootdir)/java/ini4j.jar
	install -m 775 $(M2REPO)/com/github/spullara/cli-parser/cli-parser/1.1.2/cli-parser-1.1.2.jar $(DESTDIR)$(datarootdir)/java
	ln -sf $(DESTDIR)$(datarootdir)/java/cli-parser-1.1.2.jar $(DESTDIR)$(datarootdir)/java/cli-parser.jar
	#Run script
	install -m 775 src/main/sh/speech2text.sh $(DESTDIR)$(bindir)/speech2text
	#Now, copy data
	for l in $(LANGUAGES); do  (cp -r data/$$l $(DESTDIR)$(datarootdir)/sphinx-lispeak-$$l ) ; done

uninstall:
	rm -rf $(DESTDIR)$(bindir)/speech2text
	rm -rf $(DESTDIR)$(datarootdir)/java/$(JARLINK)
	rm -rf $(DESTDIR)$(datarootdir)/java/$(JARNAME)
	#We do not remove dependencies... Very Windows-style...
	for l in $(LANGUAGES); do  (rm -rf $(DESTDIR)$(datarootdir)/sphinx-lispeak-$$l ) ; done

clean:
	mvn clean

