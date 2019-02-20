#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/4 04:39
# @Author  : LookBack
# @Site    : http://www.dwhd.org
# @File    : spirder.py
# @Software: PyCharm Community Edition
# code is far away from bugs with the god animal protecting I love animals. They taste delicious.
 
import urllib2
import re
import os
 
class Spider(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/text/page/%s?s=4997049'
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
 
    def get_page(self,page_index):
        headers = {'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url=self.url%str(page_index), headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()
 
    def analysis(self, content):
        pattern = re.compile('<a href="/article/(\d{9})" target="_blank" class=\'contentHerf\' >.<div class="content">.{4}<span>(.*?)</span>', re.S)
        # print re.findall(pattern, content)
        items = re.findall(pattern, content)
        return items
 
    def save(self, items, path):
        for item in items:
            item_new = item[1].replace('\n', '').replace('<br/>', '\n')
            path = 'qiubai'
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = path+'/'+item[0]+'.txt'
            f = open(filepath, 'w')
            f.write(item_new)
            f.close()
 
    def run(self):
        print '开始抓取'
        for i in range(1, 10):
            print '抓取第'+str(i)+'页'
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items, 'qiubai')
        print '抓取完毕...'
 
if __name__ == '__main__':
    spider = Spider()
    spider.run()
