@ECHO OFF
ECHO UPDATING PLEASE CLOSE HARNESS SELECTOR PROGRAM
ECHO THEN PRESS ENTER
PAUSE
TIMEOUT /T 30 /NOBREAK
git fetch origin
git reset --hard origin/master
ECHO UPDATE COMPLETE
PAUSE


