# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

# 数据库连接字符串
DB_CONNECT_STRING = 'sqlite:///:memory:'

# 创建数据库引擎,echo为True,会打印所有的sql语句
engine = create_engine(DB_CONNECT_STRING, echo=True)

# 创建一个connection，这里的使用方式与python自带的sqlite的使用方式类似
with engine.connect() as con:
    # 执行sql语句，如果是增删改，则直接生效，不需要commit
    rs = con.execute('SELECT 5')
    data = rs.fetchone()[0]
    print "Data: %s" % data
