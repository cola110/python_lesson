# !usr/bin/python
# coding:utf-8

print "hello python"
print "hello test python"

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print tup3
x, y = 1, 10
print x
print y

import time

ticks = time.time()
print ticks,time.localtime(ticks)


import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal;

sum = lambda arg1,arg2:arg1+arg2
print sum(10,20)

print time.__doc__
