#!/usr/bin/python
# -*- coding: utf-8 -*-
def wrapper(f):
    def wrapper_function(*args, **kwargs):
	"""这个是修饰函数"""
	return f(*args, **kwargs)
    return wrapper_function

@wrapper
def wrapped():
    """这个是被修饰的函数"""
    print('wrapped')

print(wrapped.__doc__)
print(wrapped.__name__)
print(wrapped.__module__)
print(wrapped.__dict__)
#print(wrapped.__qualname__)
#print(wrapped.__annotations__)
