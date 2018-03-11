#!/bin/sh

### BEGIN INIT INFO
# Provides:        ntp
# Required-Start:  $network $remote_fs $syslog
# Required-Stop:   $network $remote_fs $syslog
# Default-Start:   2 3 4 5
# Default-Stop:    1
# Short-Description: Start NTP daemon
### END INIT INFO

#FIXME paths should be set up by make ?!?
DAEMON=/usr/local/share/java/speech2text.jar
PIDFILE=/var/run/speech2text.pid

test -x $DAEMON || exit 5


case $1 in
	start)
        if [ -e "$PIDFILE" ];
        then
            echo "Found PID file: $PIDFILE"
            echo "This means either $0 is already in execution, or it halted abnormally."
            exit 1
        fi

        java -jar $DAEMON &

        echo $! > $PIDFILE
  		;;
	stop)
        if [ -e "$PIDFILE" ];
        then
            PID=$(cat "$PIDFILE")
            kill "$PID"
            rm -f "$PIDFILE"
        fi
  		;;
	restart|reload|force-reload)
		$0 stop && sleep 2 && $0 start
  		;;
	status)
        if [ -e "$PIDFILE" ];
        then
            echo "Running (or, at least, a PID file exists)."
        else
            echo "Not running."
        fi
        ;;
	*)
		echo "Usage: $0 {start|stop|restart|try-restart|force-reload|status}"
		exit 2
		;;
esac
