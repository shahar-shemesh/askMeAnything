#!/bin/sh
while true; do
    alembic upgrade head
    if [[ "$?" == "0" ]]; then
        break
    fi
    sleep 5
done
exec gunicorn -b :4000 --access-logfile - --error-logfile - askMeAnything:app