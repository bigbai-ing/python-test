#!/usr/bin/env python

import memcache

mc = memcache.Client(['127.0.0.1:11211'],debug=0)
mc.set("foo","bar")
value = mc.get("foo")
print value
