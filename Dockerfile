FROM python:3.9.10-slim-buster

WORKDIR /code

ENV FLASK_APP=askMeAnything.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install python-dotenv gunicorn

COPY . .

EXPOSE 4000

CMD ["flask", "run"]