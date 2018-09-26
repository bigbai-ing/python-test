# coding=utf-8

import djcelery
from celery import Celery, platforms

djcelery.setup_loader()

platforms.C_FORCE_ROOT = True

CELERY_QUEUES = {
    'beat_tasks': {
	'exchange': 'beat_tasks',
	'exchange_type': 'direct',
	'binding_key': 'beat_tasks'
    },
    'work_queue': {
	'exchange': 'work_queue',
	'exchange_type': 'direct',
	'binding_key': 'work_queue'
    }
}

CELERY_DEFAULT_QUEUE = 'work_queue'
CELRY_IMPORTS = (
    'course.tasks',
)


#防止死锁
CELERYD_FORCE_EXECV = True

#设置并发的worker数量
CELERYD_CONCURRENCY = 4

#允许重试
CELERYd_ACKS_LATE = True

#每个worker 最多执行100个任务，超过会销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

#单个任务的最大运行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30
