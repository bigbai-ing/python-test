# coding=utf-8

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

#1、初始化连接
#engine = create_engine('mysql://root:mysql@localhost/mysql', echo=True)
#
#DBSession = sessionmaker(bind=engine)
#session = DBSession()
#type(session)
#ret = session.execute('desc user')
#print ret
#print ret.first()

#2、创建表
from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:mysql@localhost/tt')
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(BaseModel):
    __tablename__ = 'user1'
    user_name = Column(CHAR(30), primary_key=True)
    pwd = Column(VARCHAR(20), default='aaa', nullable=False)
    age = Column(SMALLINT(), server_default='12')
    account = Column(INT())
    birthday = Column(TIMESTAMP())
    article = Column(TEXT())
    height = Column(FLOAT())


def init_db():
    '''
    初始化数据库
    :return:
    '''
    BaseModel.metadata.create_all(engine)

def drop_db():
    '''
    删除所以数据库
    :return:
    '''
    BaseModel.metadata.drop_all(engine)

#drop_db()
#init_db()

#添加数据
user1 = User(user_name='hahaha', account=1234232)
session.add(user1)
session.commit()


#更新数据库
#1、更新单条
query = sesion.query(User)
user = query.get('hahaha')
print user.account, user.pwd
user.account = '313331'
session.flush()
