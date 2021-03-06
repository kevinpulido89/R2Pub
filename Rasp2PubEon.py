from pubnub import Pubnub
import Adafruit_DHT as dht
import time
from datetime import datetime

GPIO = 27

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f', uuid='RasPI')

my_channel = 'temp_humid'

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

def log(t,h):
    now = datetime.now()
    file = open('log.csv','a')
    file.write('%s/%s/%s,%s:%s:%s,' % (now.day, now.month, now.year, now.hour, now.minute, now.second))
    file.write(str(t) + "," + str(h))
    file.write('\n')
    file.close()

#Publish Function
def loop():
    while True:
        ph=sum(h)/len(h)
        pt=sum(t)/len(t)
        pubnub.publish(my_channel, {
            "eon":{"Temperatura":pt,"Humedad":ph}})
        t.remove(t[0])
        h.remove(h[0])
        h_temp,t_temp = dht.read_retry(dht.DHT11, GPIO)
        t.insert(len(t),t_temp)
        h.insert(len(h),h_temp)
        print ('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(pt,ph))
        log(pt,ph)
        time.sleep(1.9)

def destroy():
    pubnub.unsubscribe(my_channel)
    print("DISCONNECTED")

if __name__ == "__main__":
    h,t = Setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
