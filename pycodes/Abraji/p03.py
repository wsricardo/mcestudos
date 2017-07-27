from random import randint
secreta = randint(1, 100)
while True:
  chute = int(input('Tentativa: '))
  if chute == secreta:
    print ('Acertou', secreta)
    break
  else:
    print ('Alto' if chute > secreta else 'Baixo')
print ('Fim do jogo')
