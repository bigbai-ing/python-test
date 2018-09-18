#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import    #定义未来文件的绝对入口，而且绝对进口必须在每个模块的顶部启用
from celery import Celery #从celery导入Celery的应用程序接口

"""
首先创建了一个celery实例app,实例化的过程中，制定了任务名pj(与当前文件的名字相同)，
Celery的第一个参数是当前模块的名称，在这个例子中就是pj,后面的参数可以在这里直接指定，
也可以写在配置文件中，我们可以调用config_from_object()来让Celery实例加载配置模块，
我的例子中的配置文件起名为config.py
"""
app = Celery('pj',
	     broker='redis://localhost',
	     backend='redis://localhost',
	     include=['pj.tasks']
	     )

app.config_from_object('pj.config')   #从config.py中导入配置文件

if __name__ == '__main__':
    app.start()

