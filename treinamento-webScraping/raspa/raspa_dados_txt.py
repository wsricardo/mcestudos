import os
import csv

linhas = 0
def extrai_dotacao(t):
  k = 1
  while True:
    j = k
    k = t.find(' ', k)
    k += 1 
    if k - j > 10: break
  j = k
  k = t.find('TEOR', k)
  while not t[k].isdigit(): k = k - 1
  valores = t[j:k].replace('.', '').split()
  soma = 0
  for v in valores[: len(valores) // 2]: soma = soma + int(v)
  return soma

def extrai_teor(t):
  j = t.find('TEOR')
  if j == -1: return 'Sem Teor'
  j = j + 4
  k = t.find('Funcional', j)
  return t[j:k].lower()

def extrai_just(t):
  j = t.find('JUSTIFICATIVA')
  if j == -1: return 'Sem justificativa'
  j = j + len('JUSTIFICATIVA')
  k = t.find('Serviço de Suporte e', j)
  return t[j:k].lower()

def extrai_deputado(f, t):
  j = t.find('DEPUTADO(A)')
  if j == -1:
    j = t.find('AUTOR(ES):')
    if j == -1:
      print (f, 'perdeu o deputado')
      return 'Sem deputado', 'Sem partido'
    j = j + len('AUTOR(ES):')
  else:
    j = j + len('DEPUTADO(A)')
  k = t.find('ASSINATURA', j)
  return t[j:k].strip()

def extrai(f, csvwriter):
  global linhas
  txt = open(f, 'r').read()
  if len(txt) == 0: return
  print (f)
  if txt[:4] == 'TEOR':
    dotacao = 'Emenda' + f + 'sem dotaçoes'
    j = 4
    k = txt.find('JUSTIFICATIVA', j)
    teor = txt[j:k]
  else:
    dotacao = extrai_dotacao(txt)
    teor = extrai_teor(txt)
  justificativa = extrai_just(txt)
  emenda, ano = f.split('.')[0].split('-')
  dep = extrai_deputado(f, txt)
  row = [dotacao, teor, justificativa, emenda, ano, dep]
  linhas += 1
  csvwriter.writerow(row)
  
csvfile = open('ALSP 28-set.csv', 'w')
csvwriter = csv.writer(csvfile)

row = 'dotacao teor justificativa emenda ano deputado'.split()
csvwriter.writerow(row)
dirList = os.listdir(".")
for f in dirList:
  if f.endswith('.txt'):
    extrai(f, csvwriter)
print ('Acabou com %d linhas' %linhas)
csvfile.close()
