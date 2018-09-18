# -*- coding:UTF-8 -*-
 
'''
OpenSSL受戒礼和Freak漏洞检测脚本
 
DesignBy:XB
2016.07
'''
 
import paramiko
import os
from Tkinter import *
 
server=[]   
sjl_sign="Server certificate\n"
freak_sign="Server certificate\n"
 
ip=raw_input("Please Input Plart IP:")
username=raw_input("Username:")
pwd=raw_input("Password:")
 
def ReadServerlist():
    print "The Plart：%s（Confirm Platform Always Online）"%ip
    if os.path.exists("serverlist.txt"):
        print "Find The Existing Serverlist."       
    else:
        print "Didn't Find The Existing Serverlist,We Will Create It."
        create=open("serverlist.txt",'w')
        create.close()
ReadServerlist()
 
def scan():
    read=file("serverlist.txt","r")
    for line in read.readlines():
        server.append(line)
    for i in server:
        i=i.strip("\n")    #去掉行末换行符
        cmd_sjl="openssl s_client -connect"+" "+i+":443 -cipher RC4" 
        cmd_freak="openssl s_client -connect"+" "+i+":443 -cipher EXPORT"
        print "\nScanning %s..."%i
        scanbody(ip,username,pwd,cmd_sjl,cmd_freak)
        
    print "\nAll Done"
    print "@Colasoft2016"
 
 
def scanbody(ip,username,pwd,cmd_sjl,cmd_freak):
    try:
 
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
        ssh.connect(ip,22,username,pwd)
 
        stdin,stdout,stderr=ssh.exec_command(cmd_sjl)
        sjl=stdout.readlines()
        stdin,stdout,stderr=ssh.exec_command(cmd_freak)
        freak=stdout.readlines()
        ssh.close()
 
        list_sjl=[]
        list_freak=[]
 
        for k in sjl:
            list_sjl.append(k)
            
 
        for j in freak:
            list_freak.append(j)
           
 
        if sjl_sign in list_sjl:
            if freak_sign in list_freak:
                print "危险：服务器存在OpenSSL受戒礼漏洞和Freak漏洞"
            else:
                print "危险：服务器存在OpenSSL受戒礼漏洞"
        else:
            if freak_sign in list_freak:
                print "危险：服务器存在OpenSSLFreak漏洞"
            else:
                print "恭喜：服务器不存在OpenSSL受戒礼漏洞和Freak漏洞"
        
 
    except paramiko.AuthenticationException,e:
        print 'Error'
        print 'Error Detail',e
 
    
 
#GUI Program
root=Tk()
root.title("OpenSSL受戒礼和Freak漏洞检测程序")
root.geometry('380x380')    #设置窗口大小，中间是x
root.resizable(width=False,height=False)    #设置窗口是否可以变化长宽，此处宽高不可变；
 
notice1=Label(root,text="请输入需要扫描的服务器IP(每行一个IP)",fg='red')
notice1.pack(side=TOP)
#滚动条
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.set(1,5)
 
#获取文件内容
content=file("serverlist.txt","r")
readtext=content.read()
content.close()
 
#写入到文件
server_list=Text(root,width=35,height=22,yscrollcommand=scrollbar.set)
server_list.place(x=5,y=80)
server_list.insert(END,readtext)
scrollbar.config(command=server_list.yview)
 
#保存函数
def save():
    save=server_list.get('0.0',END).strip()
    print "Save："
    print save
    file_object=open("serverlist.txt","w")
    file_object.writelines(save)
    file_object.close()
#保存和扫描按钮
save_button=Button(root,text="保存",width=9,height=2,command=save).place(x=260,y=80)
scan_button=Button(root,text="扫描",width=9,height=2,command=scan).place(x=260,y=150)
 
root.mainloop()
