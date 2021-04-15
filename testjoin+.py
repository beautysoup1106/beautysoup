import time

start_time=time.perf_counter()
s=''
for i in range(0,1000000):
    s+=str(i)
end_time=time.perf_counter()

print('str cost:{}'.format(end_time-start_time))

start_timejoin=time.perf_counter()
l=[]
for n in range(0,1000000):
    l.append(str(n))

l=''.join(l)
end_timejoin=time.perf_counter()

print('join cost:{}'.format(end_timejoin-start_timejoin))


start_timemap=time.perf_counter()

s=''.join(map(str,range(0,1000000)))

end_timemap=time.perf_counter()

print('map cost:{}'.format(end_timemap-start_timemap))