#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Dissassembly.
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori

import dis

# Função a ser passada para dis, disassemblar.
def add(a,b):
    r = 0
    r = a + b
    return r

dis.dis(add)
