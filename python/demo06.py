import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.ptt.cc/bbs/C_Chat/index.html"    # 第一頁

# 開啟csv檔案
with open("ptt.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    # 寫入欄位名稱
    writer.writerow(["標題", "作者"])

    for i in range(10):
        print(f"第{i+1}頁：")
        response = requests.get(url) # 取得C_Chat的HTML原始碼
        root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

        articles = root.find_all("div", class_="r-ent")    # 所有文章
        for article in articles:
            title = article.find("div", class_="title").text.strip()    # 文章標題
            author = article.find("div", class_="author").text      # 文章作者

            print(title, author)

            writer.writerow([title, author])    # 寫入一行資料

        url = "https://www.ptt.cc/"+root.find("a", string="‹ 上頁")["href"] # 換頁