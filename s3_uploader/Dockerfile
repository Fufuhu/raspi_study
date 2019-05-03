FROM python:3.6-alpine


ENV AWS_ACCESS_KEY_ID dummy
ENV AWS_SECRET_ACCESS_KEY dummy
ENV TARGET_DIR /tmp

RUN adduser notifier -D
USER notifier
WORKDIR /home/notifier

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --user

COPY src ./
CMD python ./main.py
