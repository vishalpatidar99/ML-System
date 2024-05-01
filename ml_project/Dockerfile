FROM python:3.12.2-slim

# 1. Disable python process buffering
ENV PYTHONUNBUFFERD 1

# 2. Change working directory to /app/server
WORKDIR /app/server
ADD . /app/server

ARG DEV=false


RUN pip install --upgrade pip && pip install -r requirements.txt
RUN sh compile_proto.sh

CMD python manage.py runserver 0.0.0.0:8000
