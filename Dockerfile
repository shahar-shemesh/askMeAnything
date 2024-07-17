FROM python:slim

COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install python-dotenv && pip install gunicorn

COPY . .

RUN chmod a+x boot.sh


EXPOSE 4000

ENTRYPOINT ["./boot.sh"]