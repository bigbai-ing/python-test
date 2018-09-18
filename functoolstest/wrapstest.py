# /usr/bin/env Python3
# -*- encoding:UTF-8 -*-
 
from functools import wraps
 
def sum_add(*args1): #我们要给我们的装饰器decorator，带上参数
    print '2222'
    def decorator(func):
        @wraps(func) #加上这句，原函数func被decorator作用后，函数性质不变
        def my_sum(*args2): #注意，参数要和原函数保持一致，真正实行扩展功能的是外层的装饰器
	    print '233232'
            my_s = 0
            for n in args1:
                my_s = my_s +n #这个是我们新加的求和结果
            return func(*args2) + my_s #这个，我们在原求和函数的结果上再加上s，并返回这个值
        return my_sum #返回my_sum函数，该函数扩展原函数的功能
    return decorator  #返回我们的装饰器
 
@sum_add(10,20) #启用装饰器 对sum函数进行功能扩展 
def sum(*args):
    s = 0
    print 'lllll'
    for n in args:
        s = s+n
    return s
print(sum(1,2,3,4,5))
print(sum.__name__)

