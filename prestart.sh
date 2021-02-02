echo "Hello world!"
#celery multi start w1 -A main.celery -l info --pidfile=/var/run/%n.pid --logfile=/data/logs/w1.log
#celery multi start w2 -A main.celery -l info --pidfile=/var/run/%n.pid --logfile=/data/logs/w2.log