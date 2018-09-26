# coding:UTF-8

from bottle import Bottle, request
app = Bottle()
@app.get('/')
def index():
    return request.query.get('a','default')

app.run(host='0.0.0.0', port=8008, reloader=True, debug=True)
