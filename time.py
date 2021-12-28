import time
start=time.time()
print(time.asctime())#print the current time
begain=time.asctime()
print(begain)
gm=time.gmtime()
print(gm[5])
tim=gm[5]
time=0
if(begain-start==1):
    time=time+1
    print(time,'sec')
print(start)
