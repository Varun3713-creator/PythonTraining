from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)
print(soup.find_all('h1'))
print(soup.find_all('table'))
print(soup.find_all('a'))