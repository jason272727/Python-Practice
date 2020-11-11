# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:25:11 2020

@author: User
"""
res=0
while True:
    try:
        choice=int(input('請選擇轉換溫度類型。1為華氏轉攝氏，2為攝氏轉華氏:'))
    except:
        print('輸入錯誤!輸入必須為「1」或「2」')
    else:
        if (choice<1)|(choice>2):
            print('輸入超出選項範圍')
        else:
            break
while True:
    if choice==1:
        try:
            tem=float(input('請輸入華氏溫度:'))
        except:
            print('輸入錯誤')
        else:
            res=(5/9)*(tem-32)
            print('攝氏溫度為:%.1f'%(res))
            break
    else:
        try:
            tem=float(input('請輸入攝氏溫度:'))
        except:
            print('輸入錯誤')
        else:
            res=(tem*(9/5))+32
            print('華氏溫度為:%.1f'%(res))
            break