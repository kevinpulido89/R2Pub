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
    while len(t) < 6:
        h_temp,t_temp = dht.read_retry(dht.DHT11, GPIO)
        h.insert(i,h_temp)
        t.insert(i,t_temp)
        i=i+1
        time.sleep(2)
    return h,t

def loop(h,t):
    while True:
        ph=sum(filter(None,h))/len(h)
        pt=sum(filter(None,t))/len(t)
        ph=round(ph,2)
        pt=round(pt,2)       

        # Write the value to your variable in Ubidots
        responseT = variableT.save_value({"value": pt})
        responseH = variableH.save_value({"value": ph})
        print (responseT[4])
        print (responseH[4])

        # Sobre-escribe array t y h
        t.pop(0)
        h.pop(0)
        h_temp,t_temp = dht.read_retry(dht.DHT11, GPIO)
        t.append(t_temp)
        h.append(h_temp)        
        time.sleep(15)

def destroy():
    print("DISCONNECTED")

if __name__ == "__main__":
    h,t = Setup()
    try:
        loop(h,t)
    except KeyboardInterrupt:
        destroy()
