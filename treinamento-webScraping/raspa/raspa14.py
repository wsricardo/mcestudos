from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
  html = urlopen('http://en.wikipedia.org' + articleUrl)
  bsObj = BeautifulSoup(html, 'html.parser')
  return bsObj.find('div', {'id': 'bodyContent'}).findAll('a',
                          href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
  newArticle = random.choice(links).attrs['href']
  print (newArticle)
  links = getLinks(newArticle)
