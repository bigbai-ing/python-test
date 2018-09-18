#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import
from datetime import timedalta

#CELERY_RESULT_BACKEDN = 'redis://127.0.0.1:6379/5'
#BROKER_URL = 'redis://127.0.0.1:6379/6'

CELERY_TIMEZONE = 'Asia/Shanghai'

#CELERY_ROUTES = {
#    'pj.tasks.add':{'queue': 'for_add', 'routing_key': 'for_add'},
#    'pj.tasks.subtract': {'queue': 'for_subtract', 'routing_key': 'for_subtract'},
#    }

CELERYBEAT_SCHEDULE = {
    "add": {
	    "task": "pj.tasks.add",
	    "schedule": timedelta(seconds=10),
	    "args": (100,100)
    },
}
