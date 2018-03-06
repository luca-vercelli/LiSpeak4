#!/bin/bash

#FIXME shouldn't lispeak be a service?


#FIXME paths should be set up by make ?!?
jarlocation=/usr/local/share/java
pidlocation=/var/run


if [ -e "$pidlocation/lispeak.pid" ];
then
	echo "Found PID file: $pidlocation/lispeak.pid"
	echo "This means either $0 is already in execution, or it halted abnormally."
	exit 1
fi

java -jar $(jarlocation)/speech2text.jar &

echo $! > $(pidlocation)/$0.pid

