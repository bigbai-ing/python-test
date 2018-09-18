import loader
import server


class WSGIService(object):
    def __init__(self, configname, appname):
	self.loader = loader.Loader(configname, appname)
	self.app = self.loader.loadapp_file()
	self.server = server.Server(self.app, '0.0.0.0', 8000)

    def start(self):
	self.server.start()

    def wait(self):
	self.server.wait()

    def stop(self):
	self.server.stop()

if __name__ == "__main__":
    configname = 'configure.ini'
    appname = 'main'
    server = WSGIService(configname, appname)
    server.start()
    server.wait()
