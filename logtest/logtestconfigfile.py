#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.config

logging.config.fileConfig('logging_config.ini')

# create logger
#logger = logging.getLogger('root')
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
