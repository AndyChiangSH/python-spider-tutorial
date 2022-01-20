import requests

url = "https://andychiangsh.github.io/python-spider-tutorial/web/"

response = requests.get(url)
print(response.text)
print(response.status_code)