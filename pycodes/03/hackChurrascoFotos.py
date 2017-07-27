#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Hackeando fotos dum churrasco
# Page http://afterfest.com.br
# http://www.afterfest.com.br/guten-bier-lancamento-temporada-cafe-de-la-musique/
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori


import urllib.request
tag = 'guten-bier-lancamento-temporada-cafe-de-la-musique/'
site = 'http://afterfest.com.br/'
k = texto.find(tag)
while k != -1:
  j = k + len(tag)
  if texto[j] != 'm': #não é mini foto (thumbnail)
    f = texto.find('"', j)
    print (texto[j:f])
    url = site + texto[k:f]
    foto = urllib.request.urlopen(url).read()
    file = open(texto[j:f], 'wb')
    file.write(foto)
    file.close()
    
  k = texto.find(tag, k + 1)
  
