from paste.deploy import loadapp
import os
class Loader(object):
    def __init__(self, configname, appname):
	self.configname = configname
	self.appname = appname

    def loadapp_file(self):
	wsgi_app = loadapp('config:%s' % (os.path.abspath(self.configname)), self.appname)
	return wsgi_app
