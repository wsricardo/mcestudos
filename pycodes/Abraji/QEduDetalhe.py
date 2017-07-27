import urllib.request
import json
url = 'http://educacao.dadosabertosbr.com/api/escola/'
codigo = '35805555'
resp = urllib.request.urlopen(url+codigo).read()
resp = json.loads(resp.decode('utf-8'))
print (resp['nome'])
print ('Salas:', resp['salasExistentes'])
print ('Computadores:', resp['computadores']+resp['computadoresAdm']+resp['computadoresAlunos'])
print ('Formação Docente:', resp['formacaoDocente'])
print ('Funcionários:', resp['funcionarios'])
