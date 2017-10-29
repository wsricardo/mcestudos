import requests
from bs4 import BeautifulSoup

url='http://www.sjc.sp.gov.br/secretarias/mobilidade_urbana/horario-e-itinerario.aspx?acao=p&opcao=1&txt='
url_site = 'http://www.sjc.sp.gov.br'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tabelas = soup.findAll('table', class_='textosm')
for tabela in tabelas:
  lista_tds = tabela.findAll('td')
  for item in lista_tds:
    if item.next_element.name == 'a':
      url_it = url_site +
               item.next_element.get('href')
      print (url_it)
    else:
      print (item.next_element)
  
