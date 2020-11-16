# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:05:45 2020

@author: User
"""

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]="Microsoft JhengHei"
plt.figure(figsize=[12,10])
plt.subplot(221)
size=[14,16,8,13,16,12,16,5]
labels=['商業理財','文學小說','藝術設計','人文科普','語言電腦','心靈養生','生活風格','親子共享']
colors=['red','brown','purple','blue','gray','yellow','green','pink']
plt.title('圖書分類男性銷售比率-圓餅圖',fontsize=15)
plt.pie(size,labels=labels,colors=colors,autopct='%2.1f%%',pctdistance=0.7,labeldistance=1.1,startangle=90)

plt.subplot(222)
size=[10,19,6,10,13,13,20,9]
labels=['商業理財','文學小說','藝術設計','人文科普','語言電腦','心靈養生','生活風格','親子共享']
colors=['red','brown','purple','blue','gray','yellow','green','pink']
plt.title('圖書分類女性銷售比率-圓餅圖',fontsize=15)
plt.pie(size,labels=labels,colors=colors,autopct='%2.1f%%',pctdistance=0.7,labeldistance=1.1,startangle=90)

plt.subplot(223)
width=0.25
listx=['商業理財','文學小說','藝術設計','人文科普','電腦語言','心靈養生','生活風格','親子共享']
listy1=[14,16,8,13,16,12,16,5]
listy2=[10,19,6,10,13,13,20,9]
listx1=[x-width/2 for x in range(len(listx))]
listx2=[x+width/2 for x in range(len(listx))]
plt.title('圖書分類男女性銷售-長條圖',fontsize=15)
plt.bar(listx1,listy1,width,color='b',label='男姓')
plt.bar(listx2,listy2,width,color='r',label='女姓')
plt.xlabel('圖書種類',fontsize=10)
plt.ylabel('購買人數比率',fontsize=10)
plt.xticks(range(len(listx)),labels=listx,rotation=45)
plt.yticks(range(0,25,5))
plt.legend()

plt.subplot(224)
listx=['商業理財','文學小說','藝術設計','人文科普','電腦語言','心靈養生','生活風格','親子共享']
listy1=[14,16,8,13,16,12,16,5]
listy2=[10,19,6,10,13,13,20,9]
plt.plot(listx,listy1,'b-.o',lw=1,label='男性')
plt.plot(listx,listy2,'r:s',lw=1,label='女性')
plt.xticks(range(len(listx)),labels=listx,rotation=45)
plt.yticks(range(0,25,5))
plt.grid(color='k',linestyle=':',lw='1',alpha=0.5)
plt.title('圖書分類男女銷售-折線圖',fontsize=15)
plt.xlabel('圖書種類',fontsize=10)
plt.ylabel('購買人數比率',fontsize=10)
plt.legend()