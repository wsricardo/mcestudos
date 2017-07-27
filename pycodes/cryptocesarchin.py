#!/usr/bin/python3
# CryptoCesárChines
# Criado por menina de 12 anos
# do projeto CEDET Decolar (com Prof Masanori)
def esconde(msg):
    s = ''
    for c in msg: s += chr( ord(c) + 30000 )
    return s
def mostra(msg):
    s = ''
    for c in msg: s += chr( ord(c) - 30000 )
    return s
