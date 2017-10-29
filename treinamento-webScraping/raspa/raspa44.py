import requests
import matplotlib.pyplot as plt
import pandas as pd
#adaptado do original em JavaScript do Prof. Sergio Costa
palavra = 'corrupção'
anoi = '1921' #pode ser desde 1921
anof = '2017'
url = 'http://acervo.folha.uol.com.br/resultados/'+anoi+'/'+anof+'?periodo=acervo&q=+'+palavra+'+&x=0&y=0'
page = requests.get(url)
resp = page.content.decode('utf-8')
title = 0
pags = []
ano = []
while True:
  title = resp.find('title', title)
  if title == -1: break
  print (resp[title+8: title+12])
  j = resp.find('<span>', title)
  k = resp.find('página', j)
  pg = resp[j+6: k]
  print (pg)
  pg = pg.replace('.', '')
  pags.append(int(pg))
  ano.append(int(resp[title+8: title+12]))
  title = k + 7
s = pd.Series(pags, index=ano)
s.plot()
plt.title("Menções da palavra "+palavra)
plt.xlabel('Ano')
plt.ylabel('Número de menções')
plt.show()
