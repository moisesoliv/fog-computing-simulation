#!/bin/bash

# python notifier.py &
echo "Starting fog..."
# flask run --host=0.0.0.0 --port=$FLASK_PORT
# flask run --host=127.0.0.1 --port=$FLASK_PORT
mosquitto -d
python mqtt_sub.py
echo "...Done"
