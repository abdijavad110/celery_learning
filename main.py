from proj.tasks import *
from celery import group, chain, chord

# s_add = add.s(2)
# result = s_add.delay(4)

# s_add = add.s(2, 4)
# res = s_add.delay()
# print(res.get())

# k = app.control.inspect(['worker2@javad-surfbook'])


for i in range(10):
    s1 = add.signature((i, 1))
    scheduler.apply_async([s1])





# for i in range(5):
#     s1 = mul.s(i, 1)
#     scheduler.delay(s1)
# add.apply_async((1, 2), link=mul.s(3))
# print(k.active())


# print(result.get())
