import json
import requests
from bs4 import BeautifulStoneSoup
with open ("task5.json","r+")as f:
    a=json.load(f)
# print(a)    
def analyse_movies_language(a):
    dict={}
    for i in a:
        # print(i)
        if "Language" in i:
            Language=i["Language"]
            # print(Language)
            for i in Language:
                # print(i)
                if i not in dict:
                    dict[i]=1    
                else:
                    dict[i]+=1
        else:
            continue
    # print(dict)    
    with open ("task6.json","w+")as f1:
        json.dump(dict,f1,indent=4)
analyse_movies_language(a)                        
