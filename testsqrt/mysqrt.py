#coding:UTF-8
from numpy import *
def sqrt2(x):
    s = 1.0
    kmax = 100
    tol = 1.e-14
    
    for k in range(kmax):
        
        s0 = s
        s = 0.5*(s + x/s)
        print "第",k + 1,"次迭代之后s的值是",s
        delta_s = s - s0
        if abs(delta_s / x) < tol:
            break
                 
    print k + 1,"次迭代之后s的值是",s

