#!/usr/bin/env python
# coding=utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
# 其配置过程主要分为两个部分：一是描述我们要处理的数据库表的信息，二是将我们的Python类映射到这些表上. 使用Declarative参与ORM映射的类需要被定义成为一个指定基类的子类，这个基类应当含有ORM映射中相关的类和表的信息。这样的基类我们称之为declarative base class
Base = declarative_base()

# 定义User对象:
# 有了一个基类，我们可以基于这个基类来创建我们的自定义类了。我们以建立一个用户类为例子。从Base派生一个名为User的类，在这个类里面我们可以定义将要映射到数据库的表上的属性
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 类声明完成后，Declarative将会将所有的Column成员替换成为特殊的Python访问器(accessors)，我们称之为descriptors。这个过程我们称为instrumentation，经过instrumentation的映射类可以让我们能够读写数据库的表和列。
# 此时构建好User类后，生成表信息，叫做table metadata。描述这些信息的类叫做Table，它属于Metadata的一部分


# 初始化数据库连接:
# create_engine返回的是一个Engine实例，它代表了指向数据库的一些非常核心的接口。他会根据你选择的数据库配置而调用对应的DBAPI。
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
# 添加到session，多个就多次添加add,或者session.add_all([User(), User(), User()])进行添加
session.add(new_user)
# 上面的操作都会被记录下来，可以通过相应的方法查看，例如session.new 查看新的添加，session.dirty 查看更改.
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
