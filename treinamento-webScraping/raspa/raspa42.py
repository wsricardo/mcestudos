import requests
from bs4 import BeautifulSoup

response = requests.get ("http://www.billboard.com/charts/hot-100")

bsoup = BeautifulSoup(response.content, "html.parser")

charts = bsoup.findAll("div", class_="chart-row__container")

for m in charts:
  print (m.find('h2').string, end = ' ')
  if 'a class' in str(m):
    print (m.find('a').string.strip())
  else:
    print (m.find('span').string.strip())

