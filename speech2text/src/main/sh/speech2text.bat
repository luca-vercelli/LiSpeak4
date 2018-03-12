@echo off

set DAEMON=speech2text-0.1.jar

REM in a real Windows distribution, probably all deplendencies will be copied in some /lib folder
set M2REPO=%userprofile%\.m2\repository
set CLASSPATH=.
set CLASSPATH=%CLASSPATH%;%M2REPO%\edu\cmu\sphinx\sphinx4-core\5prealpha-SNAPSHOT\sphinx4-core-5prealpha-SNAPSHOT.jar
set CLASSPATH=%CLASSPATH%;%M2REPO%\org\ini4j\ini4j\0.5.4\ini4j-0.5.4.jar
set CLASSPATH=%CLASSPATH%;%M2REPO%\com\github\spullara\cli-parser\cli-parser\1.1.2\cli-parser-1.1.2.jar
set CLASSPATH=%CLASSPATH%;%DAEMON%

java org.lispeak.speech2text.AppCli

