#/usr/bin/env python
#coding=utf-8

import bottle
from bottle import route, run
from bottle import template, view

@route('/login')
def login():
    return template('login') #login是模板的名称，不需要后戳名.tpl


@route('/info')
@view('info')   #在这里用view来加载info模板，记得这里不需要写模板后缀名
def info():
    name='彭昊'
    age=30
    blog='wwww'
    qq='898339'
    book = ['python','linux','php']
    price = {'pc':4000,'phone':2000,'bike':600}
    data = {'tname':name,'tage':age,'tblog':blog, 'tqq': qq,'tbook':book,'tprice':price,'tnum':''}
    print bottle.TEMPLATE_PATH, dir(bottle.TEMPLATES)
    return data
#    return template('info', tname=name, tage=age, tblog=blog, tqq=qq)

run(host='0.0.0.0', port=8080, debug=True)
