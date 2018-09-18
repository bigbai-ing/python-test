#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import partial

def add(x, y):
    return x+y

# 这里创造了一个新的函数add2，只接受一个整型参数，然后将这个参数统一加上2
add2 = partial(add, y=2)
print add2(3)
