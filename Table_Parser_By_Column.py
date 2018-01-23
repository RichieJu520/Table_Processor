print 'This script is written for parsing tab-delimited textfile by column!'
import os
import time, sys
Parameters=raw_input("Enter two parameters: [TextFile],[Column_Num] sepeated by Space: ")

while True:
    try:
        filename=Parameters.split(' ')[0]
        Num=int(Parameters.split(' ')[1])
        break
    except:
        continue
    
def making_folder(foldername):
    if os.path.exists(foldername):
        for root, dirs, files in os.walk(foldername):
            for name in files:
                os.remove(os.path.join(root,name))
    else:
        os.mkdir(foldername)

start=time.time() # Timing begins
wrerr = sys.stderr.write

print "Parsing in processing, pls wait...!"
making_folder(filename+'.parsed')

for line in open(filename,'r'):
    lis=line.split('\t')
    if len(lis)>=Num:
        f=open(filename+'.parsed'+'/'+str(lis[Num-1])+'.txt','a')
        f.write(line)
        #extract the 6 and 7 columns of each subtextfile
        #f.write(line.split('\t')[5]+'\t'+line.split('\t')[6]+'\n')
    else:
        continue
          
end=time.time()   # Timing ends
wrerr("OK, work finished in %3.2f secs\n" % (end-start))
raw_input('Press <Enter> to close this window!')
