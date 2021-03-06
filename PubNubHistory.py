#https://github.com/kevinpulido89/R2Pub.git

from pubnub import Pubnub
import time

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')

my_channel = "temp_humid"

def callback(message):
    print(message)

def loop():
    while True: 
        #Asynchronous usage
        #pubnub.history(my_channel, count=10, include_token=True, callback=callback, error=callback)
        
        #Synchronous usage
        print (pubnub.history(my_channel, count=2, include_token=False)) 
        time.sleep(2.628)

def destroy():
    print("Goodbye")

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
