#!/usr/bin/env python
import mincemeat
import time

strt_time=time.time()
ip_data=range(0,1000);


data_source = dict(enumerate(ip_data))

def mapfx(k, v):
    
    list=[]
    def isPrime(n):
        if n < 2 or n%2 == 0 and n!=2:
            return False
        if n == 2:
            return True
        else:
            for x in range(3, int(n**0.5)+1, 2):
                if n%x == 0:
                    return False
            return True
    def isPalindrome(x):
        num = str(x)[::-1]
        return str(x) == num
    
    for i in range(v*10000,(v+1)*10000):
        if isPrime(i) and isPalindrome(i):
            list.append(i) 
    yield 'number',list

def reducefx(k, vs):
    
    list=[]
    for i in vs:
        list.extend(i)
    return list

s = mincemeat.Server()
s.datasource = data_source
s.mapfn = mapfx
s.reducefn = reducefx

results = s.run_server(password="changeme")
print results
print len(results['number'])
print("--- time taken : %s seconds ---" % (time.time() - strt_time))
