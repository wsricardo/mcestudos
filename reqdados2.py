#!/usr/binpython3
import sys
import time
import pprint
import requests

if len(sys.argv)>1:
	payload = {'idLegislatura':'55', 'pagina':str(sys.argv[1]), 'itens':'513','ordem':'asc'}
else:
	print('Faltou numero da página')
	exit(1)
	
header = {'content-type': 'application/json'}
query = 'deputados' # Campos.(deputados, proposicoes, eventos, ...)
url = 'https://dadosabertos.camara.leg.br/api/v2/'
id = 'proposicoes'

r = requests.get(url+query, params=payload, headers=header)
d = r.json()
siz = len(d['dados'])
keys = d['dados'][0].keys()
#print('Numero: %d' % siz)

#r2 = requests.get(url+str(id))
#d2 = r2.json()
#siz2 = len(d2['dados'])
#keys2 = d2['dados'][0].keys()


# Lista deputados e respectivas infos [id]
for j in range(siz):
	print('\n\n',60*'-')
	for i in keys:
		print('\n \t %s : %s' % ( i, d['dados'][j][i] ) )

# Prosições [id]
#for j in range(siz):
#	print('\n\n',40*'-')
#	for i in keys2:
#		print('\n \t %s : %s' % ( i, d2['dados'][j][i] ) )



#
#for i in d['dados']:
#	print(i)



