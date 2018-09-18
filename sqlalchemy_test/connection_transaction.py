# -*- coding:utf-8 -*-
from sqlalchemy import create_engine

# 数据库连接字符串
DB_CONNECT_STRING = 'sqlite:///root/python_test/sqlalchemy_test/db.sqlite'
engine = create_engine(DB_CONNECT_STRING, echo=True)

with engine.connect() as connection:
    trans = connection.begin()
    try:
        r1 = connection.execute("select * from User")
        r2 = connection.execute("insert into User(name, age) values(?, ?)", 'bomo', 24)
        trans.commit()
    except:
        trans.rollback()
        raise
