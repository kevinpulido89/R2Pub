#!/usr/bin/env python3
#https://github.com/kevinpulido89/R2Pub.git
from pubnub import Pubnub
import RPi.GPIO as GPIO
import time

pubnub = Pubnub(publish_key='', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f', uuid="Pi")

my_channel = "trigger"

GPIO.setmode(GPIO.BOARD)
LED = 40 #GPIO21
GPIO.setup(LED, GPIO.OUT)

def _callback(m, channel): #m=message
    a=m['Array']['Data']
    print(a)
    if a[0]==1:
        GPIO.output(LED,True)
        print(a[0])
    elif a[0]==0:
        GPIO.output(LED,False)
        print(a[0])
    else:
        print(a[0])
        GPIO.output(LED,False)

def _error(message):
    print("ERROR : " + str(message))

def connect(message):
    print("CONNECTED")

def reconnect(message):
    print("RECONNECTED")

def disconnect(message):
    print("\nDISCONNECTED")
    pubnub.unsubscribe(my_channel)
    GPIO.cleanup()

def loop():
    while True:
        pubnub.subscribe(my_channel, callback=_callback, error=_error, connect=connect, reconnect=reconnect, disconnect=disconnect)
        time.sleep(2.628)

if __name__ == "__main__":
    try:
        print (pubnub.here_now(my_channel))
        loop()
    except KeyboardInterrupt:
        disconnect("")

