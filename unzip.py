# -*- coding: utf-8 -*-
"""
Spyder Editor
破解zip密码
This is a temporary script file.
"""
import zipfile
def pojiezip(zFile,password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return 

def main():
    tag=1
    zFile=zipfile.ZipFile('passs.zip')
    passFile=open('pass.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        guess=pojiezip(zFile,password)
        if guess:
            print '[+]Password='+password+'\n'
            tag=0
            break
    if tag==1:
        print 'pass not be guessed!'
if __name__=='__main__':
    main()
         
