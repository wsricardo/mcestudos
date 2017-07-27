#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Curso Python Para Zumbis
# Professor Masanori

page = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<title> Titulo da Página </title>
</head>
<body>
Olá!
</body>
</html>'''

arquivo = open('page.html', 'w', encoding='utf-8')
arquivo.write(page)
arquivo.close()
