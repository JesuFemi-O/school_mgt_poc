FROM python:3.9

ENV pythonunbuffered=1

RUN mkdir /app

COPY ./src /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# CMD python manage.py runserver 0.0.0.0:8000

ENTRYPOINT ["sh", "./run.sh"]