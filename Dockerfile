FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#RUN pip install -r requirements.txt
RUN pip install python-dotenv && pip install gunicorn
#RUN pip install waitress

# COPY app app
# COPY migrations migrations
# COPY askMeAnything.py config.py boot.sh ./
# RUN chmod a+x boot.sh

#ENV FLASK_APP=askMeAnything.py

COPY . .
RUN chmod a+x boot.sh


EXPOSE 4000

ENTRYPOINT ["./boot.sh"]