import requests
from bs4 import BeautifulSoup

url = 'http://www1.caixa.gov.br/loterias/loterias/megasena/megasena_pesquisa_new.asp'
page = requests.get(url)
bs = BeautifulSoup(page.content, 'html.parser')

numeros_sena = [n.get_text()
                for n in bs.findAll('li')[:6]]
#print (bs.ul.getText(' '))
results = str(page.content).split('|')
print ( {'concurso': results[0],
         'premio': results[1],
         'numero_vencedores': results[3],
         'valor_vencedores': results[4],
         'data_sorteio': results[11],
         'numeros': numeros_sena})


