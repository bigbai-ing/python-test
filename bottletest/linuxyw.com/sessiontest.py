#/usr/bin/env python
#coding=utf-8
from bottle import route, run ,redirect,request,default_app
from beaker.middleware import SessionMiddleware
#设置session参数
session_opts = {
    'session.type':'file',                   # 以文件的方式保存session
    'session.cookei_expires':3600,       # session过期时间为3600秒
    'session.data_dir':'/tmp/sessions',  # session存放路径
    'sessioni.auto':True
    }
@route('/login')
def login():
    return '''
        <html>
        <head>
        </head>
        <body>
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        </body>
        </html>
    '''
@route('/login', method='POST')
def do_login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if username == 'test' and password == 'test':
                s = request.environ.get('beaker.session')  #如果帐号密码正确，则获取环境变量中的beaker.session对象，并赋值给s，然后我们就可以用字典的方式，往s里面添加一些我们要存进去的数据，如帐号名，帐号id，权限等等
		print 's=', s
                s['user'] = username
                s.save()
        return redirect('/')

@route('/')
def index():
        for k,v in request.environ.items():
                print "K:%s     V:%s" %(k,v)
        s = request.environ.get('beaker.session') #获取session
        username = s.get('user',None)   #从session中获取Key为user的值，是上面登陆的时候保存进来的
        if not username:
                return redirect('/login')
        return "欢迎你：%s" % username
app = default_app()
app = SessionMiddleware(app, session_opts)
run(app=app,host='0.0.0.0', port=8080,debug=True)
