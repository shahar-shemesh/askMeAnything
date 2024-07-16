#!/bin/bash

alembic upgrade head
exec gunicorn -b :5000 --access-logfile - --error-logfile - askMeAnything:app


#exec waitress-serve --listen=127.0.0.1:5000 askMeAnything:app