#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Author: Wandeson Ricardo
# Page: wsricardo.github.io
# Blog: wanartsci.blogspot.com

import re
import pprint
from pprint import *

# Trecho de música de Luis Gonzaga
texto = '''Eu só quero um amor
Que acabe o meu sofrer
Um xodó pra mim
Do meu jeito assim
Que alegre o meu viver'''

t = texto.split('\n')
f = []

for i in t:
    f.append(i.split())

pprint(f)
print('\n')

# Mostrando
for i in f:
    pprint(i)
