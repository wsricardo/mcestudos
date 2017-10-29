from urllib.request import urlopen
#trazer a página inteira
html = urlopen("http://www.transparencia.sc.gov.br/remuneracao-servidores-detalhe/13103612")
res = html.read().decode('utf-8')
