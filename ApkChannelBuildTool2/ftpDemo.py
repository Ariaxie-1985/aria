# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from ftplib import FTP



def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host,21)
    ftp.login(username, password)
    print(ftp.dir())
    return ftp

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__=='__main__':
    ftpconnect('10.1.201.16','','')