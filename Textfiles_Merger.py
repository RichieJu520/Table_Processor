# Merge txtfiles into one

import fileinput
import sys
import glob
import string

print 'Function: this script is designed for merging a number of fasta, txt etc. file into one!'
print 'Notice:   put all the sub-files into the same folder before running!'

Paras=raw_input("Pls enter parameters: [folder_name],[file_format](e.g. txt, fasta, fastq) sepeated by Space: ")
while True:
    try:
        foldername=Paras.split(' ')[0]
        file_format=Paras.split(' ')[1]
        filewrite=open(foldername+'.'+file_format,'w')
        break
    except:
        print 'Notice: invalid input format for parameters!' 
        Paras=raw_input("Pls enter parameters: [folder_name],[file-format] sepeated by Space: ")
i=0
for line in fileinput.input(glob.glob(foldername+"/*."+file_format)): #process muti-documents
    i+=1
    filewrite.write(line)
    if fileinput.isfirstline():
       print "------ reading %s ------\n" % fileinput.filename() #get filename

filewrite.close()

print "OK,finished! There are "+str(i)+" lines in " + foldername+'.'+file_format+'\n'
raw_input("Press <Enter> to close this window: ")
