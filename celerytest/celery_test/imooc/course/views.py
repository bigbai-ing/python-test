from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from course.tasks import CourseTask


def do(requese):
    print ' start do request'
    CourseTask.delay()
    print 'end do request'
    return JsonResponse({'result': 'ok'})
