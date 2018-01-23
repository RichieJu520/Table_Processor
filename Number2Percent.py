import os
import time, sys
import math

filename= raw_input('Enter the name of the file containing reads abundance: ')

f=open(filename+'_percent','w')
a={}
a1=[]
for line in open(filename,'r'):
    a1.append(line.strip().split('\t')[0])
    a[line.strip().split('\t')[0]]='\t'.join(line.strip().split('\t')[1:])

name = a['#Datasets'].split('\t')

for i in range(len(name)):
    name[i]=0

if '#Datasets' in a.keys():
    f.write('#Datasets'+'\t'+a['#Datasets']+'\n')
    del(a['#Datasets'])
print len(a)
a1.remove('#Datasets')
        
for item in a1:
    b=a[item].split('\t')
    for i in range(len(name)):
        name[i]+=int(b[i])

for item in a1:
    c=a[item].split('\t')
    f.write(item.replace(' ','-')+'\t')
    for i in range(len(name)):
        calculate = 100*float(c[i])/name[i]      # calculate percentage
        #try:
            #calculate = math.log(10000*float(c[i])/name[i])  # calculate log10(percentage)
        #except:
            #calculate = 0
        f.write(str(calculate)+'\t')
    f.write('\n')

print 'OK, finished'
raw_input('Press <Enter> to close this window!')

