#!/bin/bash

# python notifier.py &
echo "Starting sensor..."
# flask run --host=0.0.0.0 --port=$FLASK_PORT &
# sflask run --host= --port=$FLASK_PORT
python mqtt_client.py
echo "...Done"