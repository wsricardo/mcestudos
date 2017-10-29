from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://beans.itcarlow.ie/prices.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.strong)
print(bsObj.strong.string)

