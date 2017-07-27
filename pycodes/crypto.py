#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Crypto
arq = open('mensagem.txt', 'r')
arqcript = open('crypto.txt','w')
f = arq.read()
a = ''
for i in f:
    if i in 'aeiou':
        a = a + '*'
    else:
        a = a + i 

arqcript.write(a)
arq.close()
arqcript.close()
