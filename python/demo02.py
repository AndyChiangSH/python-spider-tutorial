import requests
from bs4 import BeautifulSoup

url = "https://andychiangsh.github.io/python-spider-tutorial/web/"  # 取得大資工網頁的HTML原始碼

response = requests.get(url)
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

# print(root.prettify())

# h1 = root.find("h1")
# print(h1)

# h2s = root.find_all("h2")
# print(h2s)    # 列表
# print(h2s[0])   # 使用索引值

# h1_h2s = root.find_all(["h1", "h2"], limit=3)
# print(h1_h2s)
# print(len(h1_h2s))

# h2 = root.find("h2", class_="this")
# print(h2)

# h2 = root.find("h2", id="this")
# print(h2)

# # 等同於root.find("h1")
# h1 = root.select_one("h1")
# print(h1)

# # 等同於root.find("h2", class_="this")
# h2 = root.select_one("h2.this")
# print(h2)

# # 等同於root.find("h2", id="this")
# h2 = root.select_one("h2#this")
# print(h2)

# # 等同於root.find_all("h2")
# h2s = root.select("h2")
# print(h2s)
# print(h2s[0])

# here = root.find("li", id="here")
# print(here)

# parent = here.find_parent()
# print(parent)

# pre_sibling = here.find_previous_sibling()
# print(pre_sibling)

# next_sibling = here.find_next_sibling()
# print(next_sibling)

# # 先找<div>再找<p>
# info_p = root.find("div", class_="info").find("p")
# print(info_p)

# # 小試身手0
# classes = root.find("ul", class_="grade3").find_all("li")
# print(classes)
# print(classes[1])

# h1 = root.find("h1")
# print(h1.text)

# img = root.find("img")
# print(img["src"])

# link = root.find("a")
# print(link["href"])

# # 下載圖片
# img = root.find("img")  # 定位img
# image = requests.get(img["src"])    # 取得src屬性
# with open(f"logo.jpg", "wb") as file:
#     file.write(image.content)   # 寫入檔案