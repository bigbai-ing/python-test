#!/usr/bin/env python
# coding=utf-8

from bottle import route, default_app, run, request
from beaker.middleware import SessionMiddleware
import json
#import pickle
import dill

session_opts = {
	'session.type':'file',
	'session.cookie_expires':300,
	'session.data_dir':'./sessions',
	'session.auto':True
	}

class ExtendJsonEncoder(json.JSONEncoder):
    def default(self, obj):
	if isinstance(obj, set):
	    return str(obj)
	return super(ExtendJsonEncoder, self).default(obj)

class PythonObjectEncoder(json.JSONEncoder):
    def default(self, obj):
	if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
	    return json.JSONEncoder.default(self, obj)
#	return {'_python_object': pickle.dumps(obj)}
	return {'_python_object': dill.dumps(obj)}

@route('/test')
def test():
    s = request.environ.get('beaker.session')
    s['test'] = s.get('test', 0) + 1
    s.save()
    res = request.environ
    new_res = {k: unicode(v).encode("utf-8")  for k,v in res.items() if v }
    js = json.dumps(new_res, sort_keys=True, indent=4, separators=(',', ':'), cls=PythonObjectEncoder)
    print js
    return 'Test conter: %d' % s['test']

app = default_app()
app = SessionMiddleware(app, session_opts)
run(app=app, host='0.0.0.0', debug=True)
