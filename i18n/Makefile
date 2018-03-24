LANGUAGES=it

#if user is not root, should run with: 
#make install prefix=~/.local exec_prefix=~
#not sure if everything will work


all:
	for f in $(LANGUAGES); do  msgfmt $$f.po -o $$f.mo ; done

mkinstalldirs:
	#TODO

install:
	#TODO

uninstall:
	#TODO

clean:
	rm *.mo

