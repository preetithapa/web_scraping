import requests
import json 
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
def scrap_top_list():
    l=[]
    maindiv=soup.find("div",class_="panel-body content_body allow-overflow")
    subdiv=maindiv.find("table",class_="table")
    alltrs=subdiv.find_all("tr")
    position=0
    for i in alltrs:
        dic={}
        alltdrs=i.find_all("td")
        for j in alltdrs:
            movie_name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dic["movie_name"]=movie_name
            rating=i.find("span",class_="tMeterIcon tiny").get_text()[3:-2]
            dic["rating"]=float(rating)
            review=i.find("td",class_="right hidden-xs").get_text()
            dic["review"]=int(review)
            year=i.find("a",class_="unstyled articleLink").text[-5:-1]
            dic["year"]=int(year)
            url_add="https://www.rottentomatoes.com/m/"+movie_name
            dic["position"]=position
            dic["url"]=url_add
            if dic not in l:
                position+=1
                l.append(dic)
    with open("task1.json","w+") as file:
        json.dump(l,file,indent=4)
    return l
scrap_top_list()
