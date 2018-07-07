import os, csv, time, random
def beep(f,d):
    os.system('beep -f %s -l %s' % (f,d))

with open('musica.txt') as csvfile:
    dataOrig = list(csv.reader(csvfile))
    mark=[]
    for k in dataOrig:
        mark.append(k[:13])
    mark=mark[:13]
    for i in range(len(mark)):
        for j in range(len(mark[i])):
            mark[i][j]=int(mark[i][j])
            mark[j][i]=mark[i][j]

print(mark)

duration=200
n=1

data=[13/2]

for i in range(75):
    m=mark[data[len(data)-1]]
    s=0
    r=random.random()*sum(m)
    for j in range(len(m)):
        s+=m[j]
        if r <= s:
            data.append(j)
            break


for i in range(len(data)-1):
    if data[i]!=0 and data[i+1]!=0:
        for j in range(1,n+1):
            f=200+(data[i]+(data[i+1]-data[i])*j/n)*20 #change(200->400)
            beep(f, duration/n) if i>0 else time.sleep(duration/1000) #change(20->10)
    #list(map(lambda x: x*duration/20, range(20))):

    #beep(200+i*20, duration) if i>0 else time.sleep(duration/1000)
