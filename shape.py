#!/usr/bin/env python
#coding:utf-8

raws = int(raw_input('输入列数: '))
i = j = k =1 #声明变量，i由于控制外围循环（图形行数),j 用于控制空格的个数，k用于控制*的个数

#等腰直角三角形1
for i in range(0,raws):
	for k in range(0,raws - i):
		print ' * ',
		k +=1
	i +=1;
	print "\n"
#倒立等腰三角形
for i in range(0,raws):
	for k in range(0,i + 1):
		print ' * ',
		k +=1
	i +=1;
	print "\n"

#打印实心等边三角形

for i in range(0,raws +1):
	for j in range(0,raws -i):
		print " ",
		j +=1
	for k in range(0,2 * i -1): 
		if k==0 or k == 2 * i -2 or i == raws





























#def my_print(args):
#    print args
#
#def move(n, a, b, c):
#    my_print ((a, '-->', c)) if n==1 else (move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))
#
#move (3, 'a', 'b', 'c') 
