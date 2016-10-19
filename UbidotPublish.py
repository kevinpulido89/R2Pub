#!/usr/bin/python3
# Librerias
import os
import time
import Adafruit_DHT as dht
from ubidots import ApiClient

# Variables
GPIO = 27

# Create an ApiClient object
api = ApiClient(token='faApU0YBjSMIl3mBHDigaqs6bFvnR0')

# Get a Ubidots Variable
variableT = api.get_variable('57d97d357625424f07b976b3')
variableH = api.get_variable('57d97d3b7625424fa22d3595')

def Setup():
    print("Initializing... Please wait.")
    h=[]
    t=[]
    i=0
    while len(t) < 5:
        h_temp,t_temp = dht.read_retry(dht.DHT11, GPIO)
        h.insert(i,h_temp)
        t.insert(i,t_temp)
        i=i+1
        time.sleep(2)
    return h,t

def loop(h,t):
    while True:
        ph=sum(h)/len(h)
        pt=sum(t)/len(t)
        #pt *= 1.43

        # Write the value to your variable in Ubidots
        responseT = variableT.save_value({"value": pt})
        responseH = variableH.save_value({"value": ph})
        print (responseT)
        print (responseH)

        t.remove(t[0])
        h.remove(h[0])
        h_temp,t_temp = dht.read_retry(dht.DHT11, GPIO)
        t.insert(len(t),t_temp)
        h.insert(len(h),h_temp)
        
        time.sleep(15)

def destroy():
    print("DISCONNECTED")

if __name__ == "__main__":
    h,t = Setup()
    try:
        loop(h,t)
    except KeyboardInterrupt:
        destroy()
