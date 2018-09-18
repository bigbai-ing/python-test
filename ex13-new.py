# -*- coding: utf-8 -*-
from sys import argv

script, first, second, third = argv

print "Your infomation is as follows: "
a = raw_input("Please enter your %s : " % first)
b = raw_input("Please enter your %s : " % second)
c = raw_input("Please enter your %s : " % third)
print "So, your %s is a, your %s is b, your %s is c." % (first, second, third)
