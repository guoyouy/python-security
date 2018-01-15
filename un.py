# -*- coding: utf-8 -*-
"""
Spyder Editor
破解zip密码
This is a temporary script file.
"""
import optparse
import zipfile
import sys
def pojiezip(zFile,password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return 

def main():
    parser=optparse.OptionParser("usage:"+"-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options,args)=parser.parse_args()
    if (options.dname==None)|(options.zname==None):
        print parser.usage
        exit(0)
    else:
        zname=options.zname
        dname=options.dname
    tag=1
    zFile=zipfile.ZipFile(zname)
    passFile=open(dname)
    for line in passFile.readlines():
        password=line.strip('\n')
        guess=pojiezip(zFile,password)
        if guess:
            print '[+]Password='+password+'\n'
            tag=0
            break
    if tag==1:
        print '[-]pass not be guessed!'
if __name__=='__main__':
    main()
         
