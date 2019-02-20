from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# 连接数据库
engine = create_engine('mysql+pymysql://root:mysql@127.0.0.1:3306/alembictest')
 
 
Base = declarative_base()
 
class My_Table(Base):
    # 表名
    __tablename__ = 'RRDXinPlanList'
 
    # 字段
    id = Column(String(20), primary_key=True)
    amount = Column(String(20))
    earnInterest = Column(String(20))
    expectedYearRate = Column(String(20))
    fundsUseRate = Column(String(20))
    planId = Column(String(20))
    name = Column(String(20))
    status = Column(String(20))
    subpointCountActual = Column(String(20))
 
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

