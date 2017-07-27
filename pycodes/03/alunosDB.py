#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Criando um Banco de Dados Alunos.
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori

import sqlite3

# Criando a base de dados alunos.bd
con = sqlite3.connect('alunos.bd')
cur = con.cursor()
# Criando tabela 'alunos'
cur.execute(''' CREATE TABLE alunos
                (text, real)''')
# Executando comando para inserir no banco de dados
cur.execute('insert into alunos values("massanori", 42)')
cur.execute('insert into alunos values("emengarda", 666)')
# Selecionando campos da tabela do banco de dados
cur.execute('select * from alunos')

# Capturar todos os dados.
for x in cur.fetchall():
    print(x)

# Fechar conexão com Banco de Dados.
cur.close()
con.commit()
con.close()
