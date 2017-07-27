#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Surfando no Facebook - Baixando
# fotos de contatos.
# Código desatualizado (mudanças na API Graph)
# Pode requerer autentificação.
# https://developers.facebook.com/tools/explorer
# https://developers.facebook.com/docs/graph-api/reference
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori

import urllib.request
import json
from pprint import pprint

url = 'aqui o link do perfil'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
pprint (data)
