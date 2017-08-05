#!/usr/binpython3
# By Wandeson Ricardo
# Pequeno 'samples' de estudo sobre o modulo request do Python.
import sys
import time
import pprint
import requests

payload = {'nome':0, 'partido':0, 'sigla':0}
Header = None
url = 'https://dadosabertos.camara.leg.br/api/v2/'
id = 'proposicoes'

r = requests.get(url+'deputados')
d = r.json()
siz = len(d['dados'])
keys = d['dados'][0].keys()

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



