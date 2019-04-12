#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import os
import psutil
# import sys
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("fog/#")

def on_message(client, userdata, msg):
    #if msg.payload.decode() == "Hello world!":
    # os.system("clear")
    print("Received message on topic " + str(msg.topic))
    print("CPU load: ", psutil.cpu_percent())
    # len(msg.payload.decode())
    # client.disconnect()

client = mqtt.Client()
client.connect("127.0.0.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

time.sleep(5)

print("fog init...")

client.loop_forever()
