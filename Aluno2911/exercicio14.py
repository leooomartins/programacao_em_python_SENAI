import os

# exercicio 1

# with open('novo_diretorio','w') as novo_arquivo:
#      os.mkdir('novo_arquivo')

# with open('exemplo.txt','r') as arquivo:
#      conteúdo = arquivo.read()
#      print(conteúdo)

#exercicio 2

# novo_diretorio = 'meu_novo_diretorio'
# os.mkdir(novo_diretorio)

# print(f'Diretório "{novo_diretorio}" criado com sucesso')

#exercicio 3

# os.rename ('exemplo.txt', 'teste7.txt')

#exericio 4

# with os.scandir('meu_diretorio') as entrada:
#     for arquivo in entrada:
#         if arquivo.is_file():
#             print(f'Arquivo encontrado: {arquivo.name}')

#exercicio 5

import shutil
# shutil.copytree('meu_novo_diretorio', 'mirassol')

#exercicio 6

shutil.rmtree('c:/Users/Aluno/Desktop/aula14')