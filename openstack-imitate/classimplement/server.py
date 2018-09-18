import eventlet
import eventlet.wsgi
import greenlet

class Server(object):
    def __init__(self, app, hostname='0.0.0.0',port=0):
	self._pool = eventlet.GreenPool(10)
	self.app = app
	self._socket = eventlet.listen((hostname, port), backlog=10)
	(self.hostname, self.port) = self._socket.getsockname()
	print 'lisening on %s : %d' % (self.hostname, self.port)

    def start(self):
#	eventlet.wsig.server
	self._server = eventlet.spawn(eventlet.wsgi.server, self._socket, self.app, protocol=eventlet.wsgi.HttpProtocol,
			    custom_pool=self._pool)

    def stop(self):
	if self._server is not None:
	    self._pool.resize(0)

    def wait(self):
	try:
	    self._server.wait()
	except greenlet.GreenletExit:
	    print 'WSGI server has stopped.'

