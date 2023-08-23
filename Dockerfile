FROM python:3.11.4-buster

ARG AUTHOR="mik"

ARG UID

RUN groupadd -r flask && useradd -r -g flask flask

COPY ./app /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

USER flask

WORKDIR /app

ENTRYPOINT ["python", "./src/app.py"]
