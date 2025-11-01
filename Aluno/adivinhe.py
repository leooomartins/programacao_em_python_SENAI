import random

numero = random.randrange(1,11)
escolha = int(input('Escolha um número de 1 à 10 '))

if numero == escolha:
    print('Você ganhou o jogo! ')
    print('O número aleatório é: ', numero)
else:
    print('Você perdeu :( ')
    print('O número aleatório é: ', numero)