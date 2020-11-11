# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:41:52 2020

@author: User
"""

def func1(m):
    res1=1
    for i in range(1,m+1):
        res1=res1*i
    return res1
inputm=int(input('請輸入m:'))
resm=func1(inputm)
inputn=int(input('請輸入n:'))
resn=func1(inputn)
resn2=func1(inputm-inputn)
finalres=resm/(resn*resn2)
print('總共有:%d種方法'%(finalres))