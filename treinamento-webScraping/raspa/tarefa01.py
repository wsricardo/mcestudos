

from urllib.request import urlopen
from bs4 import BeautifulSoup
#imprimir apenas o h1 e o seu conteúdo líquido
html = urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.strong)
print(bsObj.strong.getText())
