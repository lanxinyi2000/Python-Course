# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:18:45 2021

@author: 26950
"""

import requests 
from bs4 import BeautifulSoup 

def down(start):
    url = ("https://book.douban.com/subject/35223102/comments/?start=%s&limit=20&status=P&sort=new_score" % start)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
    
    r = requests.get(url=url,headers=header)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    f = open("《目光》短评.txt",mode = "a",encoding='utf-8') #append追加写
    
    
    #我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，
    #用到的方法是soup.select()，返回类型是 list
    comments_list = []
    #通过类名拿到评论内容
    comment_nodes = soup.select('.comment-content')
    for node in comment_nodes:
        comments_list.append(node.get_text().strip().replace("\n", ""))
    for i in range(len(comments_list)):
        f.write(comments_list[i])
        f.write('\n')
    #测试能爬多少页，发现只能爬到前11页的评论数据    
    # page = start/20+1
    # tip = "以上是第%s页的内容" % page
    # f.write(tip)
    # f.write('\n')
    
start = 0
for i in range(100):
    down(start)
    start += 20
    




