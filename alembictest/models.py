#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    
    person_id = Column(Integer, primary_key=True)
    nickname = Column(String(64), nullable=False)
    password = Column(String(16))
    gender = Column(Integer)
    birthday = Column(Date)
    realname = Column(String(64))
    idcard = Column(String(20))


class Telephone(Base):
    __tablename__ = 'telephone'
    tel_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    telphone_no = Column(String(64))


if __name__ == '__main__':
    engine = create_engine("sqlite:///test.db")
    Base.metadata.create_all(engine)

