#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Manipulando arquivos

# Cria arquivo; ou apaga se já existir salvando novo conteudo
arquivo = open( 'numero.txt', 'w')
for linha in range(1,101):
    arq.write('%d\n' % linha)
arquivo.close()

# Ler arquivo
# print(linha.rstrip())
arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# Pythonic way (do código acima).
# Obs.: 'with' fecha o arquivo após concluido.
with open('numeros.txt') as f:
    print( f.read() )
