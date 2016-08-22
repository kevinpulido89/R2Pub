from datetime import datetime

now = datetime.now()

def log(t,h):
    file = open('log.csv','a')
    file.write('%s/%s/%s;%s:%s:%s;' % (now.day, now.month, now.year, now.hour, now.minute, now.second))
    file.write("T[C];" + str(t) + ";")
    file.write("H[%];" + str(h))
    file.write('\n')
    file.close()

#file = open('log.csv','a')
#file.write('%s/%s/%s;%s:%s:%s;' % (now.day, now.month, now.year, now.hour, now.minute, now.second) + "\n")
#file.close()
