#!/usr/bin/env python
# -*- coding:utf-8 -*-

def bubble_sort(alist):
    # 结算列表的长度
    n = len(alist)
    # 外侧循环控制 从头到尾的次数
    for j in range(n - 1):
	# 使用count记录一共交换的次数，可以排除已经拍好的序列
	count = 0
	# 内层循环控制走一次的过程
	for i in range(0, n-1-j):
	    # 如果前一个元素大于后一个元素，则交换两个元素
	    if alist[i] > alist[i+1]:
		alist[i], alist[i+1] = alist[i+1], alist[i]
		count += 1
	# count ==0 代表没有交换，序列已经有序
	if 0 == count:
	    break


if __name__ == '__main__':
    alist = [12,443 ,52, 12,4,43, 322,12,4545]
    print("原列表是: %s" % alist)
    bubble_sort(alist)
    print("新列表是: %s" % alist)
