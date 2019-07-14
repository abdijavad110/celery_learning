from __future__ import absolute_import, unicode_literals
from .celery import app
from time import sleep
import proj


@app.task(queue='default')
def scheduler(task):
    worker = 'worker1@javad-surfbook'
    cnt = 0
    active = list(map(lambda q: q['name'], app.control.inspect([]).active()[worker]))
    reserved = list(map(lambda q: q['name'], app.control.inspect([worker]).reserved()[worker]))
    scheduled = list(map(lambda q: q['name'], app.control.inspect([worker]).scheduled()[worker]))
    print('  $$$  checking ...')
    while task['task'] in active + reserved + scheduled:
        cnt += 1
        print('  $$$  stopped ' + str(cnt))
        try:
            active = list(map(lambda q: q['name'], app.control.inspect([worker]).active()[worker]))
            reserved = list(map(lambda q: q['name'], app.control.inspect([worker]).reserved()[worker]))
            scheduled = list(map(lambda q: q['name'], app.control.inspect([worker]).scheduled()[worker]))
            print(active+reserved+scheduled)
        except:
            print('  $$$  breaking')
            break
        sleep(0.5)
    print('  $$$  out of while')
    add_shadow = getattr(proj.tasks, 'add')
    add_shadow.apply_async(task['args'])
    return 'task ' + task['task'] + ' scheduled'


@app.task(queue='high_priority')
def add(x, y):
    sleep(3)
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
