#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Surf Score Ranking
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori

f = open( 'surf.txt' )
notas = {}

for linha in f:
    nome, pontos = linha.split()
    notas[float(pontos)] = nome
f.close()

for nota in sorted(notas, reverse = True):
    print('%s : %4.2f' %(notas[nota], nota))
