#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Scraping ('raspagem')
# Das aulas Python Para Zumbis Prof.: Fernando Masanori

import urllib.request
import time


#urlname = 'http://beans.itcarlow.ie/prices.html'
urlname = 'http://beans.itcarlow.ie/prices-loyalty.html'
pagina = urllib.request.urlopen(urlname)
texto = pagina.read().decode('utf-8')
onde = texto.find('>$')
inicio = onde + 2
fim = inicio + 4
preço = texto[inicio:fim] # Fatiando texto (string)
print("Preço %6.2f"%float(preço))

# Verificar se o preço é menor que x, por exemplo 4.74
# DDoS - Distributed Denial Service 
# ataque que derruba um site através de grande número
# solicitações válidas.
# Com biblioteca 'time' pode-se determinar o tempo
# para verificar os preços (liberando a CPU para outros
# processos).

# Scraping, raspagem de dados, pode ser útil
# para obter informações dum site, checar noticias,
# ou verificar quando um conteúdo está disponivel
# para baixar e efetuar o download.

# import antigravity - link pra página de humor em TI/IT
# https://xkcd.com/353/

# JSON
# http://www.json.org
#import json
#urlname = 'http://api.icndb.com/jokes/random?limitto=[nerdy]
# uso  json
#       resp = urllib.request.urlopen(urlname)
#       data = json.loads(resp.decode('utf-8'))
#
#       print(data['value']['joke'])
