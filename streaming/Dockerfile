# FROM python:3.6-slim
# EXPOSE 8000
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# RUN apt-get update && apt-get install -y libglib2.0-dev libsm6 libxrender1 libxext6
# RUN  apt install libopencv-dev libcv2.4 libcvaux2.4 libcvaux-dev libhighgui-dev libhighgui2.4 libopencv-highgui-dev libopencv-highgui2.4-deb0 libopencv-imgproc2.4v5 libopencv-imgproc-dev
# COPY raspi ./raspi
# COPY streaming ./streaming
# COPY manage.py ./
# ENTRYPOINT ["/bin/sh", "-c"]
# CMD ["python manage.py runserver 0.0.0.0:8000"]
FROM debian:stretch-slim
RUN echo "deb http://ftp.jp.debian.org/debian sid main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y -t sid python3-opencv python3-pip
RUN python3 --version
RUN python3 -c 'import cv2; print(cv2.__version__)'

EXPOSE 8000
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY manage.py ./
COPY raspi ./raspi
COPY streaming ./streaming

ENTRYPOINT [ "/bin/sh", "-c" ]
CMD ["python3 manage.py runserver 0.0.0.0:8000"]