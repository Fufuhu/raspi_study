FROM resin/rpi-raspbian

RUN pip install picamera
COPY main.py ./
CMD main.py
