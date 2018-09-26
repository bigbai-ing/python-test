# -*- coding: utf-8 -*-
#from tasks import add
#
#
#if __name__ == '__main__':
#    print 'start task..'
#    result = add.delay(3, 5)
#    print 'end task...'
#    print result
from celery_app import task1
from celery_app import task2

task1.add.delay(3, 4)
task2.multiply.delay(3,4)
print 'end tasks........'
