import requests
import os
from task1 import scrap_top_list
movies=scrap_top_list()
def get_scrape_movie_details():
    for i in movies:
        path="/home/dell/Desktop/web_scrapping/movies.text"+i["movie_name"]+"text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/dell/Desktop/web_scrapping/movies.text"+i["movie_name"]+"text","w+")
            url=requests.get(i["url"])
            c1=create.write(url.text)
            create.close()
get_scrape_movie_details()