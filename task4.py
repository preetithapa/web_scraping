from os import remove
import requests
import json
from bs4 import BeautifulSoup
movie_url="https://www.rottentomatoes.com/m/toy_story_3"
def movies_detailes(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")
    tital_div=soup.find("h1",class_="scoreboard__title").get_text()
    maindiv=soup.find_all("li",class_="meta-row clearfix")
    dict={}
    l=[]
    dict["movie_name"]=tital_div
    dict["url"]=movie_url
    for i in maindiv:
        a=i.text
        b=a.split()
        # print(b)

        if "Rating:" in b:
            dict["Rating"]=b[1]
        elif "Genre:"in b:
            dict["Genre"]=b[1:]
        elif "Director:" in b:
            i = 0
            list2 = []
            while i < len(b):
                if i == 0:
                    i += 1
                    continue
                list2.append(b[i])
                i += 1
            s=""
            for i in list2:
                for j in i:
                    if j==" ":
                        continue
                    else:
                        s+=j
            list5=s.split(",")
            dict["director"] = list5
            # print(dict)
        elif "Producer:" in b:
            dict["Producer"]=b[1:]
        elif "Language:" in b:
            l.append(b[-1])
            dict["Language"]=l
        elif b[0]=="Runtime:":
            l1=[]
            for j in b:
                if j!="Runtime:":
                    s=j.strip()[:-1]
                    l1.append(s)
            k=int(l1[0]) 
            mul=k*60
            g=int(l1[1])
            sum_mul=mul+g
            dict["Runtime"]=sum_mul  
        # print(dict)    
    with open("task4.json","w+")as f:
        json.dump(dict,f,indent=6)
        return dict
 
movies_detailes(movie_url)
