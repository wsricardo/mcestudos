#!/usr/bin/python3
#!-*- coding: utf-8 -*-


# Ideogragramas chines (tabelas unicode).
# Pode iniciar em 19968.
i = 30000
l = []
k = 0
limit = 10000
while k < limit:
    l.append(chr(i+k))
    k = k + 1

print(l)

