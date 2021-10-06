# from urllib import request
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import sqlite3
import datetime


### 1단계

url = "https://dho.inven.co.kr/dataninfo2/item/"
html_contents = requests.get(url).text

print(html_contents)
### 2단계

soup = BeautifulSoup(html_contents, "html5lib")
data1 = soup.find_all("td", class_="itemname")

save_title = []
for title in data1[1].find_all("span", class_="subject-text"):
    save_title.append(title.text)

save_link = []
for link in data1[1].find_all("a"):
    save_link.append(link.get("href"))


### 3단계

now = datetime.datetime.now()
nowStr = now.strftime("%Y-%m-%d %H:%M")

raw_data = {"title": save_title, "link": save_link}
df = DataFrame(raw_data)

con = sqlite3.connect("hot_inven.db")
df.to_sql("%s" % nowStr, con)
