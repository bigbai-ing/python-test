from gevent import monkey; monkey.patch_socket()
import gevent

print 'aaaa'

def fff(n):
    for i in range(n):
	print 'bbbbb'
        print gevent.getcurrent(), i
	gevent.sleep(0)

g1 = gevent.spawn(fff, 5)
g2 = gevent.spawn(fff, 5)
g3 = gevent.spawn(fff, 5)
g1.join
g2.join
g3.join
