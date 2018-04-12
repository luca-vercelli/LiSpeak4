# LiSpeak4
Linux voice command &amp; control system based on CMU's sphinx4

**Status: work in progress**


Parts of code are from LiSpeak/Palaver.

Install as root:

	(first, install all dependencies...)
    make && sudo make install
    lispeak-settings

Uninstall with

    sudo make uninstall

In Ubuntu-based systems, dependencies can be installed as follows:

    sudo apt-get install build-essential gcc default-jdk maven python sphinxbase
    sudo apt-get install python-gi default-jre python

(dependencies on the first line are only required to build the package)
 
