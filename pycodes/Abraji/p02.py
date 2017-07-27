#usando a mesma lógica
#escolha entre os cem nomes de meninas mais frequentes
#nomes 2014.txt (não é necessário ler o arquivo basta atribuir)
while chute != sorteado:
    chute = int(input ('Tentativa: '))
    if chute == sorteado:
        print ('Ganhou!')
    else:
        if chute > sorteado:
            print ('Alto')
        else:
            print ('Baixo')
print ('Fim do jogo!')
