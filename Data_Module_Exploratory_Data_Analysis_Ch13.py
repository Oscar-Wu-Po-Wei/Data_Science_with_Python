# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:39:57 2022

@author: oscar.wu
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

titanic = pd.read_csv("titanic.csv")
print(titanic.shape)

print(titanic.describe())

print(titanic.info())

print(np.unique(titanic["PassengerId"].values).size)
titanic.set_index(["PassengerId"], inplace=True)
# print(titanic)

# 編碼方法一
# titanic["SexCode"] = titanic["Sex"].map({"male":1, "female":0})
# 編碼方法二
titanic["SexCode"] = np.where(titanic["Sex"]=="female",1,0)
print(titanic)

print(titanic["PClass"])
class_mapping = {"1st":1,
                 "2nd":2,
                 "3rd":3}
titanic["PClass"] = titanic["PClass"].map(class_mapping)


# 處理遺漏值(空值)，此例針對年齡欄位。
print(titanic.isnull().sum())
print(sum(titanic["Age"].isnull()))      # print(titanic["Age"].isnull().sum())
avg_age = titanic["Age"].mean()
print(avg_age)
titanic["Age"].fillna(avg_age, inplace=True)
print(sum(titanic["Age"].isnull()))
age_median = np.nanmedian(titanic["Age"])
print("年齡中位數(未計入nan): ", age_median)

# 實用的Coding轉換方法(與Excel的IF()架構近似)
new_age = np.where(titanic["Age"].isnull(), age_median, titanic["Age"])

titanic["Age"] = new_age

print("性別人數:")
print(titanic["Sex"].groupby(titanic["Sex"]).size())
print(titanic.groupby("Sex")["Age"].mean())
print(titanic.index)


import re
pattern = re.compile(r"\,\s(\S+\s)")
titles = []
for index, row in titanic.iterrows():
    match = re.search(pattern,row["Name"])
    if match is None:
        title = "Mrs" if row["SexCode"] == 1 else "Mr"
    else:
        title = match.group(0)
        title = re.sub(r",", "", title).strip()
        if title[0] != "M":
            title = "Mrs" if row["SexCode"] == 1 else "Mr"
        else:
            if title[0] == "M" and title[1] == "a":
             title = "Mrs" if row["SexCode"] == 1 else "Mr"
    titles.append(title)
titanic["Title"] = titles
print("")
print(np.unique(titles).shape[0], np.unique(titles))

titanic["Title"] = titanic["Title"].replace("Mlle", "Miss")
titanic["Title"] = titanic["Title"].replace("Ms", "Miss")
titanic.to_csv("titanic_pre.csv", encoding="utf-8")
print("Title 人數: ")
print(titanic["Title"].groupby(titanic["Title"]).size())
print("各組生存率: ")
print(titanic[["Title","Survived"]].groupby(titanic["Title"]).mean())

titanic = pd.read_csv("titanic_pre.csv")
print(type(titanic))
# titanic.Died = np.where(titanic.Survived==0,1,0) # Pandas doesn't allow columns to be created via a new attribute name
titanic["Died"] = np.where(titanic.Survived==0,1,0)
titanic["Died"] = np.where(titanic["Survived"]==0,1,0)

# 以"比率尺度資料(Age)"繪製"直方圖Histogram"
# titanic["Age"].plot(kind="hist", bins=15)
# df = titanic[titanic.Survived==0]
# df["Age"].plot(kind="hist", bins=15)
# df = titanic[titanic.Survived==1]
# df["Age"].plot(kind="hist", bins=15)

# 以"名目或順序尺度資料(Title,Sex,PClass)"繪製"長條圖"，分類顯示生存與死亡人數比例。
fig, axes = plt.subplots(nrows=1, ncols=2)

# df = titanic[["Survived", "Died"]].groupby(titanic["Title"]).sum()
# df.plot(kind="bar", ax=axes[0])
# df = titanic[["Survived", "Died"]].groupby(titanic["Title"]).mean()
# df.plot(kind="bar", ax=axes[1])

# df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).sum()
# df.plot(kind="bar", ax=axes[0])
# df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).mean()
# df.plot(kind="bar", ax=axes[1])

df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).sum()
df.plot(kind="bar")
df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).mean()
df.plot(kind="bar")

df = titanic.drop("PassengerId", axis=1)
df = df.drop("Died", axis=1)
df = df.drop("Title", axis=1)
print(df.columns)
print(df.corr())