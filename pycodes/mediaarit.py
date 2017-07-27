#!/usr/bin/python3
#-*-coding: utf-8 -*-

# Media aritmética.
def media(lnums):
    notas = lnums
    med = 0
    k = 0

    while k < len( lnums ):
        med = med + lnums[k]
        k = k + 1

    med = med/( len( lnums ) )
    return med
