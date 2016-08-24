#!/usr/bin/env python3
from pubnub import Pubnub
import RPi.GPIO as GPIO
import time

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')

my_channel = "trigger"

GPIO.setmode(GPIO.BOARD)
Button = 38 #GPIO20
GPIO.setup(Button, GPIO.IN)
State = 0

while True:
    #take a reading
    input = GPIO.input(Button)

    #if the last reading was low and this one high, print
    if ((not State) and input):
        print("Button pressed")
        pubnub.publish(my_channel,{"Array":{"Data":[input]}})
    else:
        pubnub.publish(my_channel,{"Array":{"Data":[input]}})

    #update previous input
    State = input

    #slight pause to debounce
    time.sleep(0.05)
