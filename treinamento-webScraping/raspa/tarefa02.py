from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento")
bsObj = BeautifulSoup(html.read(), 'xml')
lista = bsObj.findAll("valorTotalPrevisto")

soma = 0
for v in lista:
    print(v.string)
    soma = soma + float(v.string)

print ('Total:', soma)
