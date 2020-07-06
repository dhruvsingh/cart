 FROM python:3.7-alpine
 ENV PYTHONUNBUFFERED 1
 ADD . .
 CMD ["python", "main.py"]
