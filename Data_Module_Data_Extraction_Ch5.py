# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:55:06 2020

@author: Style
"""

from bs4 import BeautifulSoup

with open('Example.html', 'r', encoding='utf-8') as fp: #打開html檔案並以fp為代號。
    soup = BeautifulSoup(fp, 'lxml') #將fp利用BeautifulSoup函數處理，並指定給變數soup，而後soup就可以進一步進行操作。
    
print(soup)
print(type(soup)) #<class 'bs4.BeautifulSoup'>

tag_a = soup.find("a")
tag_a = soup.find(name = "a") #與上一行同義
print(tag_a) #包含標籤頭尾
print(tag_a.string) #只包含標籤文字內容

tag_p = soup.find("p")
tag_a = tag_p.find("a")
print(tag_p.a.string) #與下一行同義
print(tag_a.string)

tag_div = soup.find(id="q2")
print(tag_div.string)
tag_a = tag_div.a #同義於tag_a = tag_div.find("a")
print(tag_a.string)