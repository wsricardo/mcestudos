#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Surf Score Ranking
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori

import sqlite3 
banco = sqlite3.connect("surfersDB.sdb") 
banco.row_factory = sqlite3.Row 
cursor = banco.cursor() 
cursor.execute('''select name, average
                  from surfers
                  where age > 20
                  order by average desc''') 
linhas = cursor.fetchall()
for linha in linhas:
    print ("Nome   :", linha['name'])
    print ("Média  :", linha['average']) 
    print ()
cursor.close() 

