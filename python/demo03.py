import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/C_Chat/index.html"

response = requests.get(url) # 取得C_Chat的HTML原始碼
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

links = root.find_all("div", class_="title")    # 文章標題
for link in links:  # 用for迴圈一次迭代一個元素
    print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白