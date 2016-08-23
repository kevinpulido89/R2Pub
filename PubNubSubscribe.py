#https://github.com/kevinpulido89/R2Pub.git
from pubnub import Pubnub
import time

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')

my_channel = "temp_humid"

def _callback(message, channel):
    print(message)

def _error(message):
    print("ERROR : " + str(message))

def connect(message):
    print("CONNECTED")

def reconnect(message):
    print("RECONNECTED")

def disconnect(message):
    print("\nDISCONNECTED")
    pubnub.unsubscribe(my_channel)

def loop():
    while True:
        pubnub.subscribe(my_channel, callback=_callback, error=_error, connect=connect, reconnect=reconnect, disconnect=disconnect)
        time.sleep(2.628)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        disconnect("")
