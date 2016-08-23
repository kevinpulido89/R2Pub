from datetime import datetime
def log(t,h):
    print("Hi!")
    now = datetime.now()
    file = open('log.csv','a')
    file.write('%s/%s/%s,%s:%s:%s,' % (now.day, now.month, now.year, now.hour, now.minute, now.second))
    file.write(str(t) + "," + str(h))
    file.write('\n')
    file.close()
