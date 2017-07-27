#!/usr/bin/python3
#-*- coding: utf-8 -*-

from random import randint

participantes = ['Pedro', 'Natalia', 'João']

sorteado = randint(0,len(participantes)-1)

print("\nNome do Sorteado %s" % participantes[sorteado])
