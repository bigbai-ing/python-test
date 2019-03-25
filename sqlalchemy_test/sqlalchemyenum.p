# coding=utf-8

#import os
#print(os.path)
#print(__name__)

from enumconstant import StatusConstant
from sqlalchemy import Column, String, create_engine, Integer, Enum
#from sqlalchemy_enum34 import EnumType
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class EnumTest(Base):
    __tablename__ = 'enumtest'

    id = Column(Integer, primary_key=True)
    status = Column(Enum(StatusConstant), default=StatusConstant.aa.name)
    #status = Column(EnumType(StatusConstant), default='')

engine = create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/test')
DBSession = sessionmaker(bind=engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = DBSession()
    print(StatusConstant.bb.value) 
    enumtest = EnumTest(status='w')
    #enumtest = EnumTest()
    session.add(enumtest)
    session.commit()
    session.close()
