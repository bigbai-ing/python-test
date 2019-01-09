#!/usr/bin/python
from os import path,system
import sys,getpass
ipmi_list="/etc/impi_list"

#logging's usage:logger.error(message),logger.info(message)
def initlog():
        import logging
        logger = logging.getLogger()
        hdlr = logging.FileHandler(logfile)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.NOTSET)
        return logger
logfile=__file__.replace(r'.py','.log')
logger=initlog()

command_list=["status","start","stop","log","passwd"]

def status(ip,password):
    try:
        system("echo %s && ipmitool -I lan -H %s -U root -P '%s' power status "%(ip,ip,password))
    except OSError,error:
        logging.error(error)

def start(ip,password):
    try:
        system("echo %s && ipmitool -I lan -H %s -U root -P '%s' power on "%(ip,ip,password))
    except OSError,error:
        logging.error(error)

def stop(ip,password):
    try:
        system("echo %s && ipmitool -I lan -H %s -U root -P '%s' power off "%(ip,ip,password))
    except OSError,error:
        logging.error(error)

def log(ip,password):
    try:
        system("echo %s && ipmitool -I lan -H %s -U root -P '%s' sel list"%(ip,ip,password))
    except OSError,error:
        logging.error(error)

def passwd(ip,password):
    global newpassword
    if newpassword == "":
        newpassword = getpass.getpass("Please input new password:")
    try:
        system("echo %s && ipmitool -I lan -H %s -U root -P '%s' user set password 2 '%s'"%(ip,ip,password,newpassword))
        print "new password is %s"%(newpassword)
    except OSError,error:
        logging.error(error)

#main
if len(sys.argv)<3:
    print 'Script format:%s command password'%(sys.argv[0])
    print """passowrd startwith ' and endwith '"""
    sys.exit()

if sys.argv[1] in command_list:
    command = str(sys.argv[1])
    global newpassword
    newpassword = ""
else:
    print "command %s does not exist"%(sys.argv[1])
    print """command_list:[start|stop|status|log|passwd]
             start:power on
             stop:power off
             status:power status
             log:system event log
             passwd:change root's password """
    sys.exit()

if not path.isfile(ipmi_list):
    print "file:%s does not exist!"%(ipmi_list)
    sys.exit()
else:
    f = file(ipmi_list)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        else:
            ip = str(line[:-1])
            password = str(sys.argv[2])
            eval_r(command)(ip,password)
    f.close()
