#https://github.com/kevinpulido89/R2Pub.git

from pubnub import Pubnub
import time

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')

my_channel = 'temp_humid'

def _callback(message, channel):
    print(message)
 
def _error(message):
    print(message)

def loop():
    while True:
        s = pubnub.subscribe(my_channel, callback=_callback, error=_error)
        #h = pubnub.history(my_channel, count=100, callback=_callback, error=_error)
        print(s)
        #print(h)
        time.sleep(3.628)

def destroy():
    print("Goodbye")

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
