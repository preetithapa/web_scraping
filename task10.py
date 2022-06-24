import json
import requests
from bs4 import BeautifulSoup
with open("task5.json","r+")as f:
    movies_detaile=json.load(f)
data=movies_detaile  
def analyse_language_and_directors(data):
    dic={}
    for i in data:
        for director in i["director"]:
            # print(director)
            dic[director]={}
    # print(dic)    
    for i in range(len(data)):
        for  director in dic:
            if director in data[i]["director"]:
                for Language in data[i]["Language"]:
                    dic[director][Language]=0
    for i in range(len(data)):
        for director in dic:
            if director in data[i]["director"]:
                for  Language in data[i]["Language"]:
                    dic[director][Language]+=1
        # return dic
    with open("task10.json","w") as f:
        json.dump(dic,f,indent=4)
    # print(dic)                 
analyse_language_and_directors(data)        
