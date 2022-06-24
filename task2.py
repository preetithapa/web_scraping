import requests
import json 
from bs4 import BeautifulSoup
from requests import models
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
file=open("100movies_data.json")
movies=json.load(file)
# print(type(movies))
def group_by_year():
    dic={}
    for i in movies:
        movies_list=[]
        year=i["year"]
        if year not in dic:
            for j in movies:
                if year==j["year"]:
                    movies_list.append(j)
            dic[year]=movies_list
            # print(movies_list)    
    with open("task2.json","w+")as file1:
        json.dump(dic,file1,indent=6)
        b= json.dumps(dic)
group_by_year()  