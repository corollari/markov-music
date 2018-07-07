import os, csv, time
def beep(f,d):
    os.system('beep -f %s -l %s' % (f,d))

with open('musica.txt') as csvfile:
    dataOrig = list(csv.reader(csvfile))
    data=[]
    for k in dataOrig:
        data=data+k[:-1]
    for j in range(len(data)):
        data[j]=int(data[j])

duration=200
n=1
data=data[:50]

for i in range(len(data)-1):
    if data[i]!=0 and data[i+1]!=0:
        for j in range(1,n+1):
            f=200+(data[i]+(data[i+1]-data[i])*j/n)*20 #change(200->400)
            beep(f, duration/n) if i>0 else time.sleep(duration/1000) #change(20->10)
    #list(map(lambda x: x*duration/20, range(20))):

    #beep(200+i*20, duration) if i>0 else time.sleep(duration/1000)
