print 'This script is written for dividing a LARGE textfile named [filename] into samll ones by [sizehint](M)(refers to the desized size of small files).'

import os
from os.path import join, getsize
import time, sys

Parameters=raw_input("Pls enter two parameters: [filename],[sizehint](M), sepeated by Space: ")
# if the input format is wrong, keep on asking for new input.
while True:
    try:
        filename=Parameters.split(' ')[0]
        size=Parameters.split(' ')[1]
        break
    except:
        Parameters=raw_input("Pls enter two parameters: [filename],[sizehint](M), sepeated by Space: ")

start=time.time() # Timing begins
wrerr = sys.stderr.write

if os.path.exists(filename+'_parsing'):
    for root, dirs, files in os.walk(filename):
        for name in files:
            os.remove(os.path.join(root,name))
else:
    os.mkdir(filename+'_parsing')

filesize=str(getsize(filename))

file=open(filename,'r')
sizehint = int((float(size))*1000000)
i=0
while True:
    i+=1
    f1=open(filename+'_parsing\\'+str(i)+'-'+filename,'w')
    lines = file.readlines(sizehint)
    for line in lines:
        f1.write(line)
    if int(filesize)==int(file.tell()):
        break

file.close()
f1.close()
end=time.time()   # Timing ends
wrerr("OK, work finished in %3.2f secs\n" % (end-start))

file.close()
f1.close()

raw_input('Press <Enter> to close this window!')




