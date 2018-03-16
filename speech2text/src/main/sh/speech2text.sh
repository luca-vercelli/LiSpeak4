#!/bin/sh

#FIXME paths should be set up by make ?!?
JAVADIR=/usr/local/share/java

CLASSPATH=$CLASSPATH:$JAVADIR/speech2text.jar
CLASSPATH=$CLASSPATH:$JAVADIR/sphinx4-core-5prealpha-SNAPSHOT.jar
CLASSPATH=$CLASSPATH:$JAVADIR/ini4j-0.5.4.jar
CLASSPATH=$CLASSPATH:$JAVADIR/cli-parser-1.1.2.jar


java -cp "$CLASSPATH" org.lispeak.speech2text.AppCli &


