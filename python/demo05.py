import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/C_Chat/index.html"    # 第一頁

for i in range(10):
    print(f"第{i+1}頁：")   # 現在到第幾頁

    response = requests.get(url) # 取得C_Chat的HTML原始碼
    root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

    links = root.find_all("div", class_="title")    # 文章標題
    for link in links:
        print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白

    url = "https://www.ptt.cc/" + root.find("a", string="‹ 上頁")["href"] # 換頁