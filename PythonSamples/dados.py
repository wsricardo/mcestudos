#!/usr/bin/python3
#-*-coding:utf8 -*-

import random

escolha = [0,0]
dados = {'d1':0, 'd2':0, 'd3':0}

#lança dados
def lanc():
    return random.randint(1,6) # gerando números de 1 a 6

print("\n\tGAME\n\tJogo Dados [1-6]")
pontos = 0 # score do jogador

# Loop do game.
while True:
    # Escolha dos palpites para os dados.
    escolha[0] = int( input('Escolha dado 1: ') )
    escolha[1] = int( input('Escolha dado 2: ') )

    #lance dos dados
    dados = {   'd1': lanc(),
                'd2': lanc(),
                'd3': lanc() }
    # Testa os palpites.
    if escolha[0] in dados.values():
        pontos = pontos + 1
    elif escolha[1] in dados.values():
        pontos += 1 # forma reduzida para pontos = pontos + 1
    # Game over! Se não acertou nenhum dos dois palpites.
    else:
        break

    print('\nResultado lance de dados: ', dados['d1'], dados['d2'], dados['d3'])
    print('\nPontos: ', pontos)
    print('\n')

print('\n\tFim do Jogo!\n\tSeus Pontos:  %d' % pontos)
