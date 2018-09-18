from webob.dec import *
from webob import Request, Response
from webob import exc


class Auth(object):
    def __init__(self, app):
	self.app = app

    @wsgify
    def __call__(self, req):
	print 'Auth class'
	resp = self.process_request(req)
	if resp:
	    return resp
	return self.app(req)

    @wsgify
    def process_request(self, req):
	if req.headers.get('X-Auth-Token') != 'open-sesame':
	    return exc.HTTPForbidden()

@wsgify.middleware
def filter_factory(app, global_config, **local_config):
    return Auth(app)
