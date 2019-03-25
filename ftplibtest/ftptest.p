#!/usr/bin/env python
# coding=utf-8
from ftplib import FTP


ftp = FTP()
timeout = 30
port = 21
ip_address = '10.10.20.55'
ftp.connect(ip_address, port, timeout) #连接ftp服务器

username = 'uftp'
password = '1'
ftp.login(username, password) #登陆
dir(ftp)
print ftp.getwelcome() # 获取欢迎信息
#ftp.cwd('/home/uftp/files/testpyhonftp') # 设置ftp路径
#list = ftp.nlst() # 获取目录列表
#for name in list:
#    print(name)
#path = '/tmp/ftptest/' + name 

# 文件上传
def upload(fname):
    fd = open(fname, 'rb')
    new_name = fname.split("/")[-1]
    # ftp.cwd('/home/uftp/files/testpyhonftp')
    # ftp.storbinary("STOR %s" % new_name, fd)
    ftp.mkd("/home/uftp/files/testpyhonftp")
    ftp.storbinary("STOR %s" % ('/home/uftp/files/testpyhonftp'), fd)
    fd.close()
    print("upload finished")

if __name__ == '__main__':
    fname = '/tmp/test.txt'
    upload(fname)
