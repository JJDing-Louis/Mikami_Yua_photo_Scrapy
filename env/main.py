# python 21.2.4
# 作者:Louis Ding

import urllib.request as re
import bs4
import os
import time

print("開始下載圖片!!")
url = "https://telegra.ph/%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E9%99%90%E5%AE%9A%E4%B8%89%E4%B8%8A%E6%82%A0%E4%BA%9CYua-Mikami-%E5%86%99%E7%9C%9F%E9%9B%86%E8%A6%9A%E9%86%9299P-05-27?fbclid=IwAR2YpTxcLHnwDzOwLlcbSy8i2KcOQTDQ9Yapswj6kfQy2z3iYquXjDtDwNU"
link = re.Request(url,headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"})
with re.urlopen(link) as response:
    data = response.read().decode("utf-8")
content = bs4.BeautifulSoup(data,"html.parser")
results = content.select("img")
folder_name = "[デジタル限定]三上悠亜Yua Mikami 写真集「覚醒」"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
i=1
for link in results:
     re.urlretrieve(f"https://telegra.ph/{link['src']}",f"{folder_name}\Yua Mikami{i}.jpg")
     print(f"Yua Mikami{i}.jpg_下載完成")
     time.sleep(1)
     i+=1
print("下載完成!")




