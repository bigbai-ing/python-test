#/usr/bin/env python
# coding:utf-8 
array= [4,5,6,7,9,3,2,3,4]
L = len(array)
for i in range(L):
	for j in range(L - i):
		if array[L - j - 1] < array[ L - j - 2]:
			array[L-j-1],array[L-j-2]=array[L-j-2],array[L-j-1]
for i in range(L):
	print array[i],	
