FROM python:3.13-alpine

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY src /app

CMD python3 /app/app.py