from webob.dec import *
from webob import Request, Response

class Hello(object):
    @wsgify
    def __call__(self, req):
	return Response('hello world!\n')

def app_factory(global_config, **local_config):
    return Hello()
