#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Surf Score Ranking
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori


# Abrindo arquivo em modo leitura ('r') por padrão
f = open( 'surf.txt')
# percorrendo as linhas no arquivo
for linha in f:
    # Exibindo conteudo por linha removendo 'quebras' com
    # a função 'strip' (para ajuda vide dir(linha.strip)
    # ou help(linha.strip)
    # Funções help e dir fornecem informações sobre a
    # classes e funções/metodos de cada modulo.
    print( linha.strip() )

# Salva e fecha arquivo   
f.close()
