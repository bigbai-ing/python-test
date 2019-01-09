#!/usr/bin/env python
import redis

class TestString(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
    def test_set(self):
        rest = self.r.set('user2', 'AAA')
        print(rest)
    def test_get(self):
        rest = self.r.get('user2')
        print(rest)
        return rest


def main():
    str_obj = TestString()
    str_obj.test_set()
    str_obj.test_get()

if __name__ == '__main__':
    main()
#user1 = r.get('user1')
#print(user1)
