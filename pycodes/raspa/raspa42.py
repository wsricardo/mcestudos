import requests
from bs4 import BeautifulSoup

titulo = []
artista = []

response = requests.get ("http://www.billboard.com/charts/hot-100")

if response.status_code == 200:
  bsoup = BeautifulSoup(response.content, "html.parser")

  charts = bsoup.findAll("div", class_="chart-row__container")

  for row in charts:
    titulo.append(row.find('h2').get_text())
    artista.append(row.find('a').get_text())

  for x in range(0, 100):
    print (x+1, artista[x].strip(), titulo[x])

else:
  print ("A requisicao falhou!")
