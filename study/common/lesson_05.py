# !usr/bin/python
# coding:utf-8

print "hello python"
print "hello test python"

for x in "python":
    print x

print "letter over"

fruits = ['banana', 'apple', 'mango']

for x in fruits:
    print x

print 'fruits over'


for index in range(len(fruits)):
	print index, '\t', fruits[index]

print 'index over'

print abs(-10)
print cmp(4, 2)


import math
import random
print math.pi
print math.e
print math.ceil(4.1)


print ("a" in 'array')

print ("e" in 'array')

print r'\n'


print 'my name is %s and weight is %d' % ('blue', 120)

# import string
print "str".zfill(4)
