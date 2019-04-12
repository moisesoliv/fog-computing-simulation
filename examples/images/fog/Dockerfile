FROM python:3

RUN apt-get update && apt-get install -y \
    net-tools \
    iputils-ping \
    iproute \
    iperf3 \
    vim \
    mosquitto\
    && apt-get clean \
    && rm -rf /var/tmp/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./start.sh

# ENV FLASK_APP main.py
# ENV FLASK_PORT 4000

EXPOSE 1883

ENTRYPOINT ./start.sh

# ENTRYPOINT /bin/bash