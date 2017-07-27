#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Validação de endereço IP
# Curso Python Para Zumbis
# Professor Masanori

def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True

arq = open('IPS.txt')
validos = open('validos.txt', 'w')
invalidos = open('invalidos.txt', 'w')

for linha in arq.readlines():
    print(linha)
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)

# Salva e fecha arquivos.
arq.close()
validos.close()
invalidos.close()
