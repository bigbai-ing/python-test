# -*- coding: utf-8 -*-

import contextlib

""" 
  （1）装饰器contextmanager。该装饰器将一个函数中yield语句之前的代码当做__enter__方法执行，yield语句之后的代码当做__exit__方法执行。同时yield返回值赋值给as后的变量。
"""
#@contextlib.contextmanager
#def open_func(file_name):
#    # __enter__方法
#    print("open file:", file_name, "in __enter__")
#    file_handler = open(file_name, "r")
#
#    yield file_handler
#
#    # __exit__ 方法
#    print("close file:", file_name, "in __exit__")
#    file_handler.close()
#    return
#
#with open_func("README") as file_in:
#    for line in file_in:
#        print(line)
#        break
#

# （2）closing类。该类会自动调用传入对象的close方法。使用实例如下：
class MyOpen2(object):

    def __init__(self, file_name):
	""" 初始化方法"""
	self.file_handler = open(file_name, "r")
	return

    def close(self):
	"""关闭文件，会自动调用"""
	print("call close in MyOpen2")
	if self.file_handler:
	    self.file_handler.close()
	return

# 使用实例
with contextlib.closing(MyOpen2("README")) as file_in:
    pass
