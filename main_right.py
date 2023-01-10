# описание 
# название статьи
# фотография(+видео(except:))
# дата публикации
# ссылка на статью/новость.
# "tn-news-author-list-item-image" and "tn-image-container" - difference? need to find out(!)


import json
import csv
from bs4 import BeautifulSoup
import requests
from core.config import URL, DOMEN, HEADERS


response = requests.get(url=URL, headers=HEADERS)
# print(response.status_code) 
src = response.text 
with open("core/html/index.html", "w") as file: 
    file.write(src) 

with open("core/html/index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser")

news = soup.find_all("div", class_="tn-news-author-list-item")
teg_img = soup.find_all("div", class_ = "tn-image-container")

news_info = []
for item in news:
    try:
        title = item.find("div", class_ = "tn-news-author-list-item-text").find("span", class_ = "tn-news-author-list-title")  # статья и название статьи
        description = item.find("div", class_ = "tn-news-author-list-item-text").find("p", class_ = "tn-announce") # статья и содержание статьи
        date_time = item.find("div", class_ = "tn-news-author-list-item-text").find("li") # статья и дата публикации статьи
        news_url = DOMEN + item.find("a").get("href") # сссылка на статью
        image = item.find("div", class_ = "tn-image-container").find("img").get("src") # ссылка на картинку
    except: 
        image = item.find("div", class_ = "").find("source").get("src") # видео(!)
        information = {
        "title": title.text,
        "description": description.text,
        "date_time": date_time.text.strip(),
        "image": DOMEN + image,
        "url": news_url
        }
    else:
        information = {
        "title": title.text,
        "description": description.text,
        "date.time": date_time.text.strip(),
        "image": DOMEN + image,
        "url": news_url
        }

        news_info.append(information)


with open(f"core/json/tengrinews.json", "w", encoding="utf-8") as file:
    json.dump(news_info, file, indent=4, ensure_ascii=False)


