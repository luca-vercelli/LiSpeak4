#!/bin/bash

#FIXME shouldn't lispeak be a service?

#FIXME paths should be set up by make ?!?
pidlocation=/var/run


if [ -e "$pidlocation/lispeak.pid" ];
then
	PID=$(cat "$pidlocation/lispeak.pid")
	kill $PID
	rm "$pidlocation/lispeak.pid"
fi
