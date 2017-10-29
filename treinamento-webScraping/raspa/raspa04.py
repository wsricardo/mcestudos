from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
lista = bsObj.findAll('div', {'id':"text"})
for text in lista:
  print(text.getText())
