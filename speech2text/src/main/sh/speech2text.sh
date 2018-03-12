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
JAVADIR=/usr/local/share/java
PIDFILE=/var/run/speech2text.pid

CLASSPATH=$CLASSPATH:$JAVADIR/sphinx4-core-5prealpha-SNAPSHOT.jar
CLASSPATH=$CLASSPATH:$JAVADIR/ini4j-0.5.4.jar
CLASSPATH=$CLASSPATH:$JAVADIR/cli-parser-1.1.2.jar
CLASSPATH=$CLASSPATH:$JAVADIR/speech2text.jar


case $1 in
	start)
        if [ -e "$PIDFILE" ];
        then
            echo "Found PID file: $PIDFILE"
            echo "This means either $0 is already in execution, or it halted abnormally."
            exit 1
        fi

        java org.lispeak.speech2text.AppCli &

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
