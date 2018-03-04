# LiSpeak4
Linux voice command &amp; control system based on CMU's sphinx4

Parts of code are from LiSpeak/Palaver.

Install as root:
    make
    sudo make install
    lispeak-settings

Install in user's folder:

    ./configure --path=$HOME/bin
    make
    make install
    ~/bin/lispeak-settings

(I would like to auto-detect if user is root or not)

