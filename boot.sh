#!/bin/bash

alembic upgrade head

exec gunicorn -b :4000 --access-logfile - --error-logfile - askMeAnything:app