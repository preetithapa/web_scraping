import requests
import json
from task1 import scrap_top_list
from task4 import movies_detailes
movie=scrap_top_list()
ten_movies=movie[:100]
def get_movie_details():    
    l=[]
    for i in ten_movies:
        for j in i:
            if j=="url":
                # print(j)
                l.append(movies_detailes(i["url"]))
    with open("task5.json","w+") as file:
        json.dump(l,file,indent=4)           
get_movie_details()            
