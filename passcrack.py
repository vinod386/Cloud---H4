import sys
import hashlib
import mincemeat
import time

strt_time=time.time()
enum_data=[]
data_source={}
hex_str = sys.argv[1]
print 'Processing...'

def cust_enumerate(length, possibles):
  ret = []
  if length == 1:
    return list(possibles)
  else:
    subs = cust_enumerate(length -1, possibles)
    for ch in possibles:
      for sub in subs:
        ret.append(str(ch) + str(sub))
  return ret

enum_data=cust_enumerate(1,"abcdefghijklmnopqrstuvwxyz0123456789")+cust_enumerate(2,"abcdefghijklmnopqrstuvwxyz0123456789")+cust_enumerate(3,"abcdefghijklmnopqrstuvwxyz0123456789")+cust_enumerate(4,"abcdefghijklmnopqrstuvwxyz0123456789")


temp = ''
counter = 0
for line in enum_data:
  temp = temp + line.rstrip() + ' '
  if counter % 100000 == 0:
    temp = temp + hex_str
    data_source[counter] = temp
    temp = ''
  counter += 1
  
data_source[counter] = temp

def mapfx(k,v):
 list1={}
 import md5
 v_split=v.split()
 a=v_split[-1]
 for list1 in v_split:
   list1=list1.strip()
   hashStr=md5.new(list1).hexdigest()
   if hashStr[:5]==a:
     yield list1,a

def reducefx(k,vs):
	return vs



s=mincemeat.Server()
s.data_source = data_source
s.mapfn = mapfx
s.reducefn =reducefx

results = s.run_server(password="changeme")
print results.keys()
print("--- time taken : %s seconds ---" % (time.time() - strt_time))
