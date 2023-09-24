FROM python:3.11
WORKDIR /home/usr/app
COPY . .
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y && pip install -r requirements.txt