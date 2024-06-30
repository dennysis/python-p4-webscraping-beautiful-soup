
from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')
print(doc.select('.heading-primary'))
name = doc.select('.heading-primary')[0].name
print(name)
attr = doc.select('.heading-primary')[0].attrs
print(attr)
