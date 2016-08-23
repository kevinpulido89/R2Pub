from pubnub import Pubnub

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')

my_channel = 'temp_humid'

def _callback(message, channel):
    print(message)

def _error(message):
    print(message)

def loop():
    While True:
        s = pubnub.subscribe(my_channel, callback=_callback, error=_error)
        #pubnub.history(my_channel, count=100, callback=_callback, error=_error)
        print(s)

def destroy():
    print("Goodbye")

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()