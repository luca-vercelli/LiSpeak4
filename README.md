# LiSpeak4
Linux voice command &amp; control system based on CMU's sphinx4

Parts of code are from LiSpeak/Palaver.

Install as root:

	(first, install all dependencies...)
    make
    sudo make install
    lispeak-settings

Install in user's folder:

	(first, install all dependencies as root...)
    make
    make install prefix=~/.local exec_prefix=~
    ~/bin/lispeak-settings

Uninstall with

    sudo make uninstall

or, if installed in user's folder:

    make uninstall prefix=~/.local exec_prefix=~

