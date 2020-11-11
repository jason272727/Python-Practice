# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:11:41 2020

@author: User
"""
#註解程式碼為檢查輸出用
import math as ma
def std(lis1):
    lismin=min(lis1)
    lismax=max(lis1)
    total=0
    verm=0
    for i in range(0,len(lis1),1):
        total=total+lis1[i]
    avg=total/len(lis1)
        #var=(ver+(avg-lis1[i])**2)/len(lis1)
    #變異數
    for j in range(0,len(lis1),1):
        verm=round(verm+((lis1[j]-avg)**2),2)
        #print(verm)
    var=verm/(len(lis1)-1)
    #print(ver)
    sd=ma.sqrt(var)
    return lismin,lismax,avg,var,sd
    #print('最小值為:%d'%(lismin))
    #print('最大值為:%d'%(lismax))
    #print('平均值為:%.2f'%(avg))
    #print('變異數為:%.2f'%(var))
    #print('標準差為:%.2f'%(sd))
lis1=[5,8,9,6,4,1,5,3,6,2]
print('最小值:%d\n最大值:%d\n平均值:%.2f\n變異數:%.2f\n標準差:%.2f\n'%(std(lis1)))
