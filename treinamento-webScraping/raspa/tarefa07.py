from bs4 import BeautifulSoup
import requests
url = 'http://g1.globo.com/educacao/universidades.html'
soup = BeautifulSoup(requests.get(url).text,
                     'html.parser')

sigla = [sig.string.strip() 
         for sig in soup.findAll('td',
                          {'class':'sigla'})]
nome = [name.string.strip()
        for name in soup.findAll('td',
                          {'class':'nome'})]
uf = [estado.string.strip()
      for estado in soup.findAll('td',
                          {'class':'uf'})]

from itertools import groupby
from operator import itemgetter

universidades = [{'nome': x, 'uf': y,
                  'sigla': z}
      for x, y, z in zip(nome, uf, sigla)]

universidades.sort(key=
                   itemgetter('uf', 'nome'))
estados = groupby(universidades,
                  itemgetter('uf'))
for estado, grupamento in estados:
  print(estado)
  for univ in grupamento:
    print(univ['nome'], univ['sigla'])
  print ()
