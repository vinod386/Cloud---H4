#!/usr/bin/env python
import mincemeat
import sys
import time
strt_time = time.time()
file=open(str(sys.argv[1]),'r')
ip_data = list(file)
file.close()


data_source = dict(enumerate(ip_data))

#print the datasource

def mapfx(k,v):
    for n in v.split():
        
        yield '1',float(n)


def reducefx(n,vs):
    import math
    
    result_sum = sum(vs)
    mean = sum(vs)/len(vs)
    std = 0
    
    for i in vs:
        std = std + ((mean-i)*(mean-i)) 
    std = std/len(vs)
    return [result_sum, len(vs), math.sqrt(std)]

s=mincemeat.Server()
s.datasource = data_source
s.mapfn = mapfx
s.reducefn = reducefx

results = s.run_server(password="changeme")
print results
print time.time()-strt_time
