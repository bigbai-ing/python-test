#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests

r = requests.get('https://api.douban.com/v2/book/search?小王子')
print r.GET.items()
