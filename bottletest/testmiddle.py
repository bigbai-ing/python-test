# coding:UTF-8

from bottle import Bottle, run

app = Bottle()


@app.get('/')
def index():
    return "输出内容"


class Middle(object):
    def __init__(self, obj):
	self.app = obj
    def __call__(self, environ, start_response):
	print("请求前处理")
	r = self.app(environ, start_response)
	print("请求后处理")
	return r

app = Middle(app)

run(app=app, host="0.0.0.0", port=8009, reloader=True, debug=True)
