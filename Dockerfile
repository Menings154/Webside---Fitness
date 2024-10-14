FROM python:slim

RUN pip install pipenv --user
COPY Pipfile Pipfile 
RUN pipenv install
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY fitnesswebsite.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP microblog.py
RUN flask translate compile

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]