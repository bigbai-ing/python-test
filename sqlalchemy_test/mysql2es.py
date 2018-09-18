#!/usr/bin/env python
# coding: utf-8


import os


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from multiprocessing import Pool


class DbMgr():
    '''
    连接数据库，从数据库获取 用户表，文章表数据
    '''

    def __init__(self):
        eng = create_engine('mysql+pymysql://root:mysql@localhost/test?charset=utf8')

        # 使用 automap 自动反射出 member，article 表对应的类
        meta = MetaData()
        meta.reflect(eng, only=['member', 'article'])
        Base = automap_base(metadata=meta)
        Base.prepare()

        self._Member = Base.classes.member
        self._Article = Base.classes.article

        # 获取操作数据库的 session
        Session = sessionmaker(eng, autocommit=True)
        self._ses = Session()

    def get_data(self):
        '''
        查询用户表，文章表
        '''
        self._users = self._ses.query('"user"', self._Member.mid,
                                      self._Member.email,
                                      self._Member.nickname).all()

        self._articles = self._ses.query(self._Article).all()
        self._articles = [('ar', i.arid, i.title, i.tags, i.description)
                          for i in self._articles]

        return list(self._users) + list(self._articles)


class Searcher():
    '''
    进城处理函数，查找符合条件的结果，找到后返回结果
    '''
    def __init__(self, keyword):
        self._keyword = keyword

    def run(self, data):
        '''
        查找字符串
        '''
        try:
            if self._keyword in str(data):
                return 'ret: ' + str(os.getpid()) + '->' + str(data)
            else:
                return None
        except Exception as e:
            return e

    def callback(self, data):
        '''
        全部执行完后回调函数，展示结果
        '''
        try:
            for i in data:
                if i:
                    print('match: {}'.format(i))
        except Exception as e:
            print(e)


def main():
    # 从数据库读取数据
    mgr = DbMgr()

    # 创建过滤进程池
    pool = Pool(4)

    # 创建搜索器
    while True:
        keyword = input('\n输入搜索词:  ')
        if keyword == 'q':
            break

        searcher = Searcher(keyword)

        # 从数据库获取数据
        data = mgr.get_data()
        res = pool.map_async(searcher.run,
                             data,
                             10,
                             callback=searcher.callback)

        # 等待所有进程执行完成
        res.wait()
        print('all done', res.successful())


if __name__ == '__main__':
    main()
