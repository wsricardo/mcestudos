from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento")
bsObj = BeautifulSoup(html.read(), 'xml')
nameList = bsObj.findAll("valorTotalPrevisto")

soma = 0
for name in nameList:
    print(name.get_text())
    soma = soma + float(name.get_text())

print ('Total:', soma)
