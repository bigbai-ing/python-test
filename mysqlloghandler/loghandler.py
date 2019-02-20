# coding: utf-8
import time
import logging
import pymysql

from sqlalchemy import (Column, DateTime, Integer, MetaData,
			        String, Table, create_engine, text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker

Base = declarative_base()


class LoggerHandlerToMysql(logging.Handler):
    def __init__(self, configdb_str, table_name):
        self.config_engine = create_engine(configdb_str)
        self.ConfigSession = sessionmaker(bind=self.config_engine)
        self.config_session = self.ConfigSession()
        metadata = MetaData(self.config_engine)
        log_table = Table(table_name, metadata,
			  Column('id', Integer, primary_key=True),
			  Column('create_time', DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00.000'")),
			  Column('level_name', String(10)),
			  Column('message', String(255)),
			  Column('split_type', String(10)),
			  Column('split_base', String(10)),
			  Column('exc_info', String(255)),
			  Column('exc_text', String(255)),
			  Column('file_name', String(100)),
			  Column('line_no', Integer),
			  Column('func_name', String(255)),
			  Column('stack_info', String(255)))
        metadata.create_all(self.config_engine)
        self.LogModel = self.getModel(table_name, self.config_engine)
        logging.Handler.__init__(self)

    def formatDBTime(self, record):
        record.dbtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))

    def emit(self,record):
        self.format(record)
        log_model = self.LogModel()
        #assert isinstance(record, logging.LogRecord)
        print("LoggingHandler received LogRecord: {}".format(record))
        #self.format(record)
        self.formatDBTime(record)
        print(record.__dict__)
        #log_model.create_time = str(record.asctime).replace(",", ".")
        log_model.create_time = record.dbtime
        log_model.level_name = record.levelname
        message = record.message
        message = message.split("---")
        log_model.message = message[0].strip()
        if len(message) > 1:
            log_model.splilt_type = message[1].strip()
        if len(message) > 2:
            log_model.split_base = message[2].strip()
        log_model.exc_info = record.exc_info
        log_model.exc_text = record.exc_text
        log_model.file_name = record.filename
        log_model.line_no = record.lineno
        log_model.func_name = record.funcName
        log_model.stack_info = record.stack_info
        self.config_session.add(log_model)
        self.config_session.commit()

    def close(self):
        self.config_session.commit()
        self.config_session.close()

    def getModel(self,name, engine):
        """ 根据name创建并return一个新的model类
         name:数据库表名
         engine:create_engine返回的对象，指定要操作的数据库连接，from sqlalchemy import create_engine
        """
        Base.metadata.reflect(engine)
        table = Base.metadata.tables[name]
        t = type(name, (object,),dict())
        mapper(t, table)
        Base.metadata.clear()
        return t
 
    def createTableFromTable(name, tableNam, engine):
        """copy一个已有表的结构，并创建新的表
        """
        metadata = MetaData(engine)
        Base.metadata.reflect(engine)
        # 获取原表对象
        table = Base.metadata.tables[tableNam]
        # 获取原表建表语句
        c = str(CreateTable(table))
        # 替换表名
        c = c.replace("CREATE TABLE " + tableNam, "CREATE TABLE if not exists " + name)
        db_conn = engine.connect()
        db_conn.execute(c)
        db_conn.close()
        Base.metadata.clear()

if __name__ == "__main__":
    # 数据库连接字符串
    user = 'root'
    password = 'mysql'
    host = '127.0.0.1'
    port = '3306'
    db = 'mysqllog'
    charset = 'utf8mb4'
    configdb_str = 'mysql+pymysql://%s:%s@%s:%d/%s?charset=%s'%(user, password, host, int(port), db, charset)
    # 表名
    log_to_sql = 'service_log'
    logger = logging.getLogger()
    handler = LoggerHandlerToMysql(configdb_str, log_to_sql)
    logger.addHandler(handler)
    logger.info('just test')
    logger.error('ddd error')
