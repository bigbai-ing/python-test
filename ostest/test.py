#!/usr/bin/python
import os

abs_path = os.path.abspath(__file__)
dirname_path = os.path.dirname(abs_path)
print 'os_path_dirname', os.path.dirname(__file__)
print 'abs path=', abs_path
print 'dirname=', dirname_path

if os.path.isfile('/root/python_test/ostest/'):
    print 'ok'
else:
    print 'no'
