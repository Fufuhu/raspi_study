FROM python:3.6-slim
EXPOSE 8000
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libglib2.0-dev libsm6 libxrender1 libxext6
COPY raspi ./raspi
COPY streaming ./streaming
COPY manage.py ./
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["python manage.py runserver 0.0.0.0:8000"]