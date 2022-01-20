import requests
from bs4 import BeautifulSoup

url = "https://andychiangsh.github.io/python-spider-tutorial/web/"  # 取得大資工網頁的HTML原始碼

response = requests.get(url)
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

# print(root.prettify())

# h1 = root.find("h1")
# print(h1)

# h1 = root.find("h1", class_="this")
# print(h1)

# h1 = root.find("h1", id="this")
# print(h1)

# h2s = root.find_all("h2")
# print(h2s)    # 列表
# print(h2s[0])   # 使用索引值

# h1_h2s = root.find_all(["h1", "h2"], limit=3)
# print(h1_h2s)
# print(len(h1_h2s))

# # 等同於root.find("h1")
# h1 = root.select_one("h1")
# print(h1)

# # 等同於root.find("h1", class_="this")
# h1 = root.select_one("h1.this")
# print(h1)

# # 等同於root.find("h1", id="this")
# h1 = root.select_one("h1#this")
# print(h1)

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

# info_p = root.find("div", class_="info").find("p")
# print(info_p)

# h1 = root.find("h1")
# print(h1.getText())
# print(h1.text)
# print(h1.string)

# link = root.find("a")
# print(link["href"])
# print(link.get("href"))

# img = root.find("img")
# print(img["src"])
# print(img.get("src"))

img = root.find("img")
image = requests.get(img["src"])
# print(image.content)
with open(f"logo.jpg", "wb") as file:
    file.write(image.content)