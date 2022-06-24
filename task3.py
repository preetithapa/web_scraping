import requests
import json 
from bs4 import BeautifulStoneSoup
file=open("task1.json")
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
    return dic    
group_by_year()
dec=group_by_year()
# print(dec)
def group_by_decade(movies):
    moviesdec={}
    list1=[]
    for i in movies:
        mod=i%10
        decade=i-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    # print(list1)  
    for j in list1:
        moviesdec[j]=[]
    # print(moviesdec)
    for k in moviesdec:  
        dec10=k+9
        for x in movies:
            if x<=dec10 and x>=k:
                for v in movies[x]:
                    moviesdec[k].append(v)
    # return moviesdec                

    with open("task3.json","w+")as file2:
        json.dump(moviesdec,file2,indent=6)
        c=json.dumps(moviesdec)
        print(c)

group_by_decade(dec)
