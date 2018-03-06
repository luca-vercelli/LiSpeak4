#!/bin/bash

#FIXME shouldn't lispeak be a service?

#FIXME paths should be set up by make ?!?
pidfile=/var/run/lispeak.pid


if [ -e "$pidfile" ];
then
	PID=$(cat "$pidfile")
	kill "$PID"
	rm "$pidfile"
fi
