FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt /app/

RUN pip3 install -vvv -r /app/requirements.txt

COPY / /app/
WORKDIR /app/

RUN pip3 install python-multipart
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]
