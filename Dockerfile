FROM python:3.6

RUN pip install picamera
COPY main.py ./
CMD main.py