# import random

# n = random.randint(1,10)

# print(n)

import random

ppt_maquina = ['🪨','🧻','✂️']
ppt_jogador = ['🪨','🧻','✂️']

aleatorio = random.choice(ppt_maquina)
escolha = int(input('''
0 - 🪨
1 - 🧻
2- ✂️
'''))

if aleatorio == ppt_jogador[escolha]:
    print('empate')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])

elif aleatorio == '🧻' and ppt_jogador[escolha] == '🪨':
    print('O Computador ganhou')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])

elif aleatorio == '✂️' and ppt_jogador[escolha] == '🪨':
    print('O Computador ganhou')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])

elif aleatorio == '✂️' and ppt_jogador[escolha] == '🧻':
    print('O Computador ganhou')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])

elif ppt_jogador[escolha] == '🧻' and aleatorio == '🪨':
    print('Você ganhou')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])

elif ppt_jogador[escolha] == '🪨' and aleatorio == '✂️':
    print('Você ganhou')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])

elif ppt_jogador[escolha] == '✂️' and aleatorio == '🧻':
    print('Você ganhou')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])