FROM debian:latest
FROM python:3.9.6-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
CMD ["python3", "kelime_bot/__init__.py"] 
CMD ["python3", "__main__.py"] 
