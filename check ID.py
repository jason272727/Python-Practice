# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:50:03 2020

@author: User
"""
while True:
    iden=str(input('Please enter your ID:'))
    if (iden.isspace()==True) | (iden.isalpha()==True) | (iden.isdigit()==True) | (len(iden)!=10) | (iden.isalnum==False):
        print('Input Error!')
    else:
        break
dic1={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'J':18,'K':19,'L':20,'M':21,'N':22,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'X':30,'Y':31,'W':32,'Z':33}
fir=iden[0]
ten=dic1.get(fir)
X1=ten//10
X2=ten%10
j=8
N=0
for i in range(1,9,1):
    if j>=1:
        N=N+(int(iden[i])*j)
        j=j-1
n9=int(iden[9])
test=X1+(X2*9)+N+n9
if test%10==0:
    print('ID Correct!')
else:
    print('Wrong ID!')
