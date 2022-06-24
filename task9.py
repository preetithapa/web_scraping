import random
import time,json
with open ("task5.json","r+")as f2:
    data=json.load(f2)
movies=data
def get_movies_d(movies):
    for i in movies:
        random_sleep=random.randint(1,3)
        path=open("/home/dell/Desktop/web_scrapping/tex.text"+i["movie_name"]+"text","w+")
        data=str(i)
        creat=path.write(data)
        time.sleep(random_sleep)
        path.close()
get_movies_d(movies)
