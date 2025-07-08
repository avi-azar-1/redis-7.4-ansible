import os,re,sys

byte_modifiers={'g':10**9,'gb':1024**3,'m':10**6,'mb':1024**2,'k':10**3,'kb':1024,'b':1}
mem_sum = 0

with os.popen('egrep -i "maxmemory [1-9]" /etc/redis/*.conf 2>/dev/null') as f:
     mem=f.read()
     if mem=='':
         print('0GB')
         exit(0)
     mem=mem.strip()
     f.close()

mem_vals = [i.split(' ')[1] for i in mem.split('\n')]

for i in mem_vals:
    mem_num=int(re.findall('\d+',i)[0])
    mem_letter=re.findall('[a-z]+',i.lower())
    if len(mem_letter)>0:
         mem_letter=mem_letter[0]
    else:
         mem_letter='b'
    mem_modifier=byte_modifiers.get(mem_letter)
    mem_sum += mem_num*mem_modifier
print(str(round(float(mem_sum)/1024**3,2)) + 'GB')
