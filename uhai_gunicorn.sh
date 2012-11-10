#!/bin/bash
set -e
LOGFILE=/home/uhai/webapps/uhai/logs/uhai.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=uhai
GROUP=uhai
ADDRESS=127.0.0.1:8000
#cd /home/uhai/webapps/
#source /home/uhai/envs/guni/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS --bind=$ADDRESS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE