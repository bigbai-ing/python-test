# -*- coding: utf-8 -*-
""" 配置文件读取"""

import ConfigParser
from ConfigParser import NoSectionError,NoOptionError

CONF = ConfigParser.RawConfigParser()

def get(key, section="default", default=None):
    """获取指定配置项的字符串，若没有指定，则返回default的参数值"""
    try:
	return CONF.get(section, key)
    except (NoSectionError, NoOptionError):
	return default

def getint(key, section="default", default=None):
    """获取指定配置项的整数值，若配置项不存在时，返回default参数值"""
    try:
	return CONF.getint(section, key)
    except (NoSectionError, NoOptionError):
	return default

def options(section="default", default=None):
    try:
	retrun CONF.options(section)
    except NoSectionError:
	return default

def load(file):
    """读取配置文件"""
    CONF.read(file)
