#!/usr/bin/python3
# Librerias
import os
import time
import paho.mqtt.client as paho
import Adafruit_DHT as dht
from urllib.parse import urlparse
from pubnub import Pubnub
from datetime import datetime

# Variables
serverMosquitto = 'm12.cloudmqtt.com'
portMosquitto = 13960
userMosquitto = 'fndyggak'
passMosquitto = 'Y33UVZ8Gh_7d'
GPIO = 27
my_channel = 'temp_humid'

# Crear paquete de llaves PUBNUB
pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f', uuid='RasPI')

# Define event callbacks and Functions
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_log(mosq, obj, level, string):
    print(string)

def Setup():
    print("Setting up... Please wait.")
    h=[]
    t=[]
    i=0
    while len(t) < 5:
        h_temp,t_temp = dht.read_retry(dht.DHT11, GPIO)
        h.insert(i,h_temp)
        t.insert(i,t_temp)
        i=i+1
        time.sleep(0.5)
    return h,t

def log(h,t):
    now = datetime.now()
    file = open('log.csv','a')
    file.write('%s/%s/%s,%s:%s:%s,' % (now.day, now.month, now.year, now.hour, now.minute, now.second))
    file.write(str(t) + "," + str(h))
    file.write('\n')
    file.close()

def loop(h,t):
    while True:
        ph=sum(h)/len(h)
        pt=sum(t)/len(t)
        #pt *= 1.43
        pubnub.publish(my_channel, {
            "eon":{"Temperatura":pt,"Humedad":ph}})
        print ('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(pt,ph))
        
        # Almacena datos en log Local
        log(ph,pt)

        # Publish a message mqtt
        mqttc.publish("Temp/value", pt)
        mqttc.publish("Humid/value", ph)
		
	# Sobre-escribe array t y h
        t.pop(0)
        h.pop(0)
        h_temp,t_temp = dht.read_retry(dht.DHT11, GPIO)
        t.append(t_temp)
        h.append(h_temp)

        time.sleep(5)

def destroy():
    pubnub.unsubscribe(my_channel)
    print("DISCONNECTED")

mqttc = paho.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get(serverMosquitto, 'mqtt://localhost:1883')
url = urlparse(serverMosquitto)

# Connect
mqttc.username_pw_set(userMosquitto, passMosquitto)
mqttc.connect(serverMosquitto, portMosquitto)

if __name__ == "__main__":
    h,t = Setup()
    try:
        loop(h,t)
    except KeyboardInterrupt:
        destroy()
