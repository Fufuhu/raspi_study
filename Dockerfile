FROM resin/rpi-raspbian:latest

RUN apt-get update && apt-get install -y libraspberrypi-bin && \
    apt-get install -y python3 python3-pip && \
RUN pip3 install picamera
COPY main.py ./
CMD python main.py


