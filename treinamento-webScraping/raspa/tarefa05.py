from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.dicionariodenomesproprios.com.br/top-brasil/'
html  = urlopen(url)
bsObj = BeautifulSoup(html.read(), 'html.parser')
nomes = bsObj.findAll('ol', {'class': 'top-list'})
boys  = nomes[0]
girls = nomes[1]
for name in boys: print (name.a.get_text())
for name in girls: print (name.a.get_text())

#feito pela Augusta
