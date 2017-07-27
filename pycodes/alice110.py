#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Curso Python Para Zumbis
# Professor Masanori

# Strig e Textos - Alice Nos Pais das Maravilhas
# http://www.gutenberg.org/ebooks/11?msg=welcome_stranger

arq = open('alice.txt')
texto = arq.read()
texto = texto.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print('Alice aparece %s vezes' %dic['alice'])
arq.close()
