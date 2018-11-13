#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#多进程扫描ip段
import multiprocessing
import subprocess

#ping 网段ip
def ping_host(activeq, notactiveq, ipaddr):
    #ping [-c count] [-W timeout] [-I interface] 
    if subprocess.call('ping -c 1 -W 1 %s > /dev/null' % ipaddr, shell=True) !=0:
	activeq.put(ipaddr)
    else:
	notactiveq.put(ipaddr)

# 读取队列数据
def read(q):
    while True:
	if not q.empty():
	    value = q.get(True)
	    print value
	else:
	    break

if __name__ == '__main__':
    #创建进程间通信队列
    manager = multiprocessing.Manager()
    activeq = manager.Queue()
    noactiveq = manager.Queue()
    process_number = multiprocessing.cpu_count()
    host_list = []
    ip_segment = '192.168.204.'
    for ipnum in range(1,255):
	host_list.append( ip_segment + str(ipnum))

    # 创建进程池
    #pool = multiprocessing.Pool(processes=process_number)
    pool = multiprocessing.Pool(processes=100)
    for ipaddr in host_list:
	pool.apply_async(ping_host, args=[activeq, noactiveq, ipaddr])
    pool.close()
    pool.join()

    #输出未使用的ip
    print '未使用的ip有:'
    read(activeq)
    #输出正在使用ip
    print '已经使用的ip有:'
    read(noactiveq)
