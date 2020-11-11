# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:18:57 2020

@author: User
"""
while True:
    name=str(input('請輸入您的ID:'))
    if name=='':
        print('您未輸入您的ID')
    elif name.isspace()==True:
        print('您的ID不可全為空白')
    else:
        break
while True:
    try:
        gender=int(input('請輸入您的性別。1為女性，2為男性:'))
    except:
        print('輸入錯誤!請重新輸入')
    else:
        if(gender<1)|(gender>2):
            print('輸入錯誤，超出性別定義範圍。')
        elif gender==1:
            print('Ms.%s您好，歡迎來到猜數字遊戲!'%(name))
            break
        else:
            print('Mr.%s您好，歡迎來到猜數字遊戲!'%(name))
            break
realans=20
while True:
    try:
        playerans=int(input('請輸入一個數字:'))
    except:
        print('您的輸入必須為數字!')
    else:
        if playerans==realans:
            if gender==1:
                print('答對了!%s正妹'%(name))
                break
            else:
                print('答對了!%s帥哥'%(name))
                break
        elif playerans>20:
            if gender==1:
                print('嗨~正妹!答案還要再小一點')
            else:
                print('嗨~帥哥!答案還要再小一點')
        else:
            if gender==1:
                print('嗨~正妹!答案還要再大一點')
            else:
                print('嗨~帥哥!答案還要再大一點')