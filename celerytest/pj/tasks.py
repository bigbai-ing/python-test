#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import

from celery import Celery
from celery import group

from pj.celery import app

@app.task
def add(x, y):
    return x + y

@app.task
def subtract(x, y):
    return x - y
