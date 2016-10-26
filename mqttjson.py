#!/usr/bin/python3
# Librerias
import os
import time
import paho.mqtt.client as paho
import Adafruit_DHT as dht
from urllib.parse import urlparse

# Variables
mqtt = {
    "server":"m12.cloudmqtt.com",
    "port":13960,
    "user":"fndyggak",
    "pass":"Y33UVZ8Gh_7d"
}

# Define event callbacks and Functions
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_log(mosq, obj, level, string):
    print(string)

def loop(h,t):
    while True:
        h+=1
        t+=1
        # Publish a message mqtt
        data = {"Temp":t,"Humid":h}
        mqttc.publish("Hemeroteca/values", data)
	
        time.sleep(3)

def destroy():
    print("DISCONNECTED")

mqttc = paho.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get(mqtt["server"], 'mqtt://localhost:1883')
url = urlparse(mqtt["server"])

# Connect
mqttc.username_pw_set(mqtt["user"], mqtt["pass"])
mqttc.connect(mqtt["server"], mqtt["port"])

if __name__ == "__main__":
    try:
        loop(0,0)
    except KeyboardInterrupt:
        destroy()
