FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /solution

COPY . .

RUN chmod +x *.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
