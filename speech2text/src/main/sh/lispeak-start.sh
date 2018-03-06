#!/bin/bash

#FIXME shouldn't lispeak be a service?


#FIXME paths should be set up by make ?!?
jarlocation=/usr/local/share/java
pidfile=/var/run/lispeak.pid


if [ -e "$pidfile" ];
then
	echo "Found PID file: $pidfile"
	echo "This means either $0 is already in execution, or it halted abnormally."
	exit 1
fi

java -jar $(jarlocation)/speech2text.jar &

echo $! > $(pidfile)

