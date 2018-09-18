#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import update_wrapper

def wrapper(f):
    def wrapper_function(*args, **kwargs):
	"""这个是修饰函数"""
	return f(*args, **kwargs)
    update_wrapper(wrapper_function, f)
    return wrapper_function

@wrapper
def wrapped():
    """这个是被修饰的函数"""
    print('wrapped')

print(wrapped.__doc__)
print(wrapped.__name__)
print(wrapped.__module__)
print(wrapped.__dict__)
print(__name__)
print(update_wrapper.__name__)
#print(wrapped.__qualname__)
#print(wrapped.__annotations__)
