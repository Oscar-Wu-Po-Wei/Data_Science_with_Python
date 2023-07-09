#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:05:27 2021

@author: Serene
"""

str1 = "Oscar is Rulai."

list1 = str1.split(" ")
print(list1)

str2 = ", ".join(list1)
print(str2)

str3 = "  Oscar is \nRulai.\n\r  "
str4 = str3.replace('\n','').replace('\r','')
print("'" + str4 + "'") #印出單引號需要雙引號括住
str5 = str4.strip()
print("'" + str5 + "'")

import string

str6 = "#$%^@$*&Python -is- *a* programming!@# ^&language#$"
list2 = str6.split(" ")
for item1 in list2:
    print(item1.strip(string.punctuation))

###    
import re
list3 = ["", "/", "path/", "/path", "/path/", "//path/", "/path///"]

def getPath(path): #path為參數
    if path:
        if path[0] != "/":
            path = "/" + path
        if path[-1] != "/":
            path = path + "/"
            path = re.sub(r"/{2, }", "/", path)
        else:
            path = "/"
    return path #回傳參數

for item2 in list3:
    item2 = getPath(item2)
    print(item2)
###[此區塊執行結果與書本不符] 

#[寫入csv檔案]
import csv

csvfile = "Example.csv"
with open(csvfile, "r") as fp:
    reader = csv.reader(fp) #使用csv.reader將檔案內容讀進變數
    for row in reader:
        print(",".join(row))
        
csvfile3 = "Example3.csv"
list4 = [[10, 33, 45], [5, 25, 56]]
with open(csvfile3, "w+", newline="") as fp:
    writer = csv.writer(fp) #使用csv.writer將檔案內容寫進fp檔案
    writer.writerow(["Data1", "Data2", "Data3"]) #先寫入檔頭
    for row in list4:                            #再寫入每列資料
        writer.writerow(row)

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.w3schools.com/html/html_media.asp"
csvfile = "VedioFormat.csv"
r = requests.get(url)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text,"lxml")
tag_table = soup.find(class_="w3-table-all") #class之後不能有任何空格
rows = tag_table.findAll("tr")

with open(csvfile, "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for row in rows:
        rowList=[]
        for cell in row.findAll(["td", "th"]): #可以用清單的方式指定多個目標
            rowList.append(cell.get_text().replace("\n", "").replace("\r", ""))
        writer.writerow(rowList)
        
#[儲存成json檔案]
import json
data = {
        "name":"Oscar Wu",
        "score":"95",
        "tel":"0912345678"
        }
json_str = json.dumps(data) #字串轉字典
print(json_str)
print(type(json_str)) #str
data2 = json.loads(json_str) #字典轉字串
print(data2)
print(type(data2)) #dict

import json
jsonfile = "Example.json"
with open(jsonfile, "w") as fp:
    #json.dumps(data, fp)
    json.dump(data, fp) #沒有s
    
with open(jsonfile, "r") as fp:
    data = json.load(fp)
json_str = json.dumps(data)
print(json_str)

import json
import requests
jsonfile = "Books.json"
url = "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&projection=lite"
r =requests.get(url)
r.encoding = 'utf-8'
json_data = json.loads(r.text)
with open(jsonfile, "w") as fp:
    json.dump(json_data, fp)
    
#[SQLite]
import sqlite3
#建立資料庫連接
conn = sqlite3.connect("PD.sqlite")
c = conn.cursor()
#執行SQL指令SELECT
c.execute("CREATE TABLE Parkinson_Database (Gene, Variant, Info)")
#將資料插入資料庫
c.execute("INSERT INTO Parkinson_Database VALUES ('LRRK2', 'G2019S', 'Asian_PD')")
#取出查詢結果的每一筆紀錄
#for row in c:
#    print(row[0], row[1])
conn.commit()
conn.close() #關閉資料庫連接