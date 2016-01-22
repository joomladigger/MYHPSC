#coding:UTF-8
from numpy import *
x = 2.0
s = 1.0

for k in range(6):
    print "第",k,"次迭代之前s的值是",s
    s = 0.5*(s + x/s)
    print "第",k,"次迭代之后s的值是",s

