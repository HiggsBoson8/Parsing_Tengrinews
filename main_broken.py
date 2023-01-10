import csv
import time
import json
import random
import datetime
from os import system 

# Created module - созданный модуль
from core.config import URL, HEADERS, DOMEN

# Downloaded libraries - скачанная библиотека 
import requests
from bs4 import BeautifulSoup
# название, описание статьи, когда было создано, фотографии
# tn-news-author-list-title tn-announce tn-data-list tn-image-container

count_site = int(input("Сколько страниц спарсить: "))
for count in range(1, count_site + 1):
    response = requests.get(url = URL, headers = HEADERS, params={"page": f"page-{count}"})

    with open("core/html/index.html", "a", encoding = "UTF-8") as file: 
        file.write(response.text) 




for count in range(1, count_site + 1):
    with open("core/html/index.html", "r") as file: 
        src = file.read()

    soup = BeautifulSoup(src, "html.parser").find_all("div", class_ = "tn-news-author-section")

    with open("core/html/index.html", "w") as file:
        file.write(str(soup))




with open("core/html/index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser").find_all("a") 

news_info = []

for item in soup: 
    url_product = DOMEN + item.get("href")
    news_image = item.get("tn-image-container")
    description = item.get("data-category").replace("/", " ")
    news_url = str(item.find("span", class_ = "tn-image-container").text).strip()

    information = {
    "url": url_product,
    "name": news_image,
    "category": description,
    "new_price": news_url
    }

    news_info.append(information)

with open("core/json/asd.json", "w") as file:
    json.dump(news_info, file, indent = 4, ensure_ascii = False)


#________________________________________________________________________________


#________________________________________________________________________________
# # описание
# #название
# #фотография
# #когда была опубликована

# import json
# import csv
# from bs4 import BeautifulSoup
# import requests
# from core.config import URL, DOMEN, HEADERS


# # response = requests.get(url=URL, headers=HEADERS)
# # print(response.status_code)
# # src = response.text
# # with open("core/html/index.html", "w") as file:
# #     file.write(src)
# with open("core/html/index.html", "r") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "html.parser")

# news = soup.find_all("div", class_="tn-news-author-list-item")
# teg_img = soup.find_all('img')

# news_info = []
# for item in news:
#     title = item.find("div", class_="tn-news-author-list-item-text").find("span", class_="tn-news-author-list-title")
#     description = item.find("div", class_="tn-news-author-list-item-text").find("p", class_="tn-announce")
#     date_time = item.find("div", class_="tn-news-author-list-item-text").find("li")
#     news_url = DOMEN + item.find("a").get("href")
    
# #     print(f"""
# # {title.text} 
# # {description.text}
# # {date_time.text} 
# # {news_url}\n""")
#     for image in teg_img:
#         src = image.get("src")
#         if src:
#             image = DOMEN + src
    
#     information = {
#         "title": title.text,
#         "description": description.text,
#         "date_time": date_time.text.strip(),
#         "image": image,
#         "url": news_url
#     }
    
#     news_info.append(information)

# with open(f"core/json/tengrinews.json", "w", encoding="utf-8") as file:
#     json.dump(news_info, file, indent=4, ensure_ascii=False)