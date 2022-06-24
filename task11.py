import json 
import requests
from bs4 import BeautifulSoup
with open ("task5.json","r+")as f2:
    data=json.load(f2)
def analyse_movies_gener(data):
    l=[]
    for i in data:
        if "Genre" in i:
            b=i["Genre"]
            l.append(b)
    # print(l)
    l1=[]
    for j in l:
        if type(j)==list:
            for k in j:
                l1.append(k)
    # print(l1)
    l2=[]
    for i in l1:
        str=""
        for j in i:
            if j==",":
                pass
            else:
                str+=j
        l2.append(str)
    # print(l2)  
    l3=[]
    for j in l2:
        if j not in l3:
            l3.append(j)
    # print(l3)
    l4=[]
    for i in l3:
        if i=="&":
            pass
        else:
            l4.append(i)
    # print(l4)
    dic={}
    for i in l4:
        c=0
        for j in l2:
            # print(j)
            if i==j:
                c+=1
        dic[i]=c
    print(dic)
    with open("task11.json","w+")as f:
        json.dump(dic,f,indent=4)
analyse_movies_gener(data)        
