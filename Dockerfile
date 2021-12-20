FROM python:3.10-slim

WORKDIR /opt/app-root/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /opt/app-root/app

EXPOSE 8000
