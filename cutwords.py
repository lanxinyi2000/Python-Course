# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 08:48:36 2021

@author: 26950
"""

import jieba
import re
#from collections import Counter
import pandas as pd
from wordcloud import WordCloud

content = ""
result = "result_com.txt"
r = '[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;：。？、 ~@#￥%……&*（）]+'
f = open('./《目光》短评.txt','r',encoding='utf-8')
content = re.sub(r," ",f.read())

count = jieba.lcut(content)

#定义空字典，对分词结果先去除通用词，再进行词频统计
stopwords = [line.strip() for line in open('./cn_stopwords.txt', 'r', encoding='utf-8').readlines()]
word_count={}
comment_data=''
for word in count:
    if word not in stopwords:
        if word != ' ':
            word_count[word] = word_count.get(word,0) + 1
            if word != '\t':
               comment_data += word
               comment_data += " "

#按词频对分词进行排序
items = list(word_count.items())
items.sort(key=lambda x: x[1], reverse=True)

#输出词频结果
pd.DataFrame(items).to_csv('frequency.csv')

#生成词云图
wordcloud=WordCloud(width=3000, height=3000, background_color="white", margin=10,
                    max_words=150, min_font_size=100, max_font_size=800, repeat=False,
                    font_path="C:\Windows\Fonts\simkai.ttf").generate(comment_data) 
wordcloud.to_file('目光.jpg')

