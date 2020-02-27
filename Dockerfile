FROM python:3.7-buster

RUN pip install Flask

COPY init.py / 

ENV FLASK_ENV="development"
ENV FLASK_APP="init.py"

CMD flask run --host 0.0.0.0