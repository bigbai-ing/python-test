#! /usr/bin/env python2.7
# -*- coding: utf8 -*
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

def get_database(host, db_name, user, password):
    db_type = 'mysql+pymysql'
    string = '%s://%s:%s@%s/%s' % (db_type, user, password, host, db_name)
    db_engine = create_engine(string, echo=True)
    Base = automap_base()
    Base.prepare(db_engine, reflect=True)
    tables = Base.classes
    return db_engine, tables
    

def get_session():
    db_engine = get_databases(host, db_name, user, password)
    DBSession = sessionmaker(bind=db_engine)
    session = DBSession
    return session, db_table

def query_data(db_name, table_name, filter_condition, **kw)
    session, db_table = get_session(db_name)
    query_result = session.query(db_table.table_name).filter(db_table.table_name.filter_condition).all()
    session.close()
    return query_result

if __name__ == '__main__':
    query_result = query_data()
