# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:44:31 2020

@author: User
"""
mstep=1
nstep=1
diffstep=1
res=0
while True:
    try:
        m=int(input('Please enter m:'))
    except:
        print('input error')
    else:
        break
while True:
    try:
        n=int(input('Please enter n:'))
    except:
        print('input error')
    else:
        nm=m-n
        for im in range(1,m+1,1):
            mstep=mstep*im
        for jn in range(1,n+1,1):
            nstep=nstep*jn
        for di in range(1,nm+1,1):
            diffstep=diffstep*di
        res=mstep/(nstep*diffstep)
        print('ans:',res)
        break
    