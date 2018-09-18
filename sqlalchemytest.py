#!/usr/bin/env python
# coding=utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/test')
# 创建DBSession类型:这里返回的是一个class，不是一个实例。
#创建数据，需要一个游标，叫做sessionmaker。
DBSession = sessionmaker(bind=engine)
#以上是完成初始化和具体每个表的class定义，如果有多个表，则定义多个clss类即可。

#添加 一条记录
# 创建session对象的实例，也就是cursor游标:
session = DBSession()
# 创建新User对象:
new_user = User(id='8', name='Faker8')
# 添加到session，多个就多次添加add:
session.add(new_user)
# 一同提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

#查询数据库
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
session.close()

#修改
#原理是先查询出来，然后赋值
session = DBSession()
data = session.query(User).filter(User.id>5).filter(User.id<7).first()
print(data)
data.name = "Jack Liu"
data.password = "Shit happends"

session.commit()
session.close()
