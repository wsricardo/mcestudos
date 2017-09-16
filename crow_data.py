#!/usr/bin/python3
#
# Author: Wandeson Ricardo
# Manipulate json
#
import json
import urllib.request
import matplotlib

# Datas
data = None
# URL Page from datas sources.
#url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'
url = 'http://api.pgi.gov.br/api/1/serie/2531.json'

# Get connection with API or web page
resp = urllib.request.urlopen(url).read()

# Get data json.
data = json.loads(resp.decode('utf-8'))
k = 0
print(data['url'],data['nome'])
print('\n')
print('\n ',data['nome_estendido'],'\n ', data['nome'],'\n ', data['descricao'])
#print('\n ', data['valores'][0]['estado_ibge'],'\n')
print('Codigo Estado IBGE - Ano - Valor (R$)')
for i in data.keys() :
    #print('\ni: ', i)
    #print('\ndata: ', data[i])
    if i == 'valores':
            #print('\n',10*'-')
            #print('\n Valores', data)
            #print('\n ',data[i][0]['estado_ibge'], ' ', data[i][0]['ano'],' ', data[i][0]['valor'])
            for j in range(0,len(data[i])):
                #print('\n valores -> keys', data[i][j].keys())
                print('\n ',data[i][j]['estado_ibge'], ' ', data[i][j]['ano'],' ', data[i][j]['valor'])
