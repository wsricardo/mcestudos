from urllib.request import urlopen
from bs4 import BeautifulSoup
#imprimir apenas o h1 e o seu conteúdo líquido
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.h1)
print(bsObj.h1.getText())
