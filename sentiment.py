#import os
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np


comment = []
f = open('./《目光》短评.txt','r',encoding='utf-8')
rows = f.readlines()
for row in rows:
    if row not in comment:
        comment.append(row.strip('\n'))

#调用SnowNLP计算每一条评论的情感值
sentimentslist = []
for li in comment:
    print(li)
    s = SnowNLP(li)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)
    
#生成情感值分布直方图
plt.hist(sentimentslist,bins=np.arange(0, 1.01, 0.01))
plt.xlabel("The comments distribution")
plt.ylabel('sentiment count')
plt.show()

#print(sentimentslist)

#统计积极消极情感分布
for i in range(len(sentimentslist)):
    if (sentimentslist[i] > 0.5):
        sentimentslist[i] = 1
    else:
        sentimentslist[i] = -1
#print(sentimentslist)
info = []
a = 0
b = 0
for x in range(0, len(sentimentslist)):
    if (sentimentslist[x] == 1):
        a = a + 1
    else:
        b = b + 1
info.append(b)
info.append(a)
#print(info)
info2 = ['negative', 'positive']
plt.bar(info2, info, tick_label=info2, color='#2FC25B')
plt.xlabel("comments analyst")
plt.show()

