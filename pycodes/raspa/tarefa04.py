from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://sismpconsultapublica.mpsp.mp.br/ConsultarDistribuicao/ObterFiltrosPorMembro')

bsObj = BeautifulSoup(html.read(), 'html.parser')
nameList = bsObj.findAll('option')
membros = {}
for name in nameList[1:-5]:
    membros[name.get_text()] = name['value']
    print (name.get_text(), name['value'])

