from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'html.parser')
for link in bsObj.find('div', {'id': 'bodyContent'}).findAll('a',
                          href=re.compile('^(/wiki/)((?!:).)*$')):
  if 'href' in link.attrs:
    print (link.attrs['href'])

#Estão dentro do div com o id = bodyContent
#Urls começam com /wiki/ e não tem :
