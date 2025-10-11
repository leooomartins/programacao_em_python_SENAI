lista_alunos = []
nome1 = input('Nome 1: ')
nome2 = input('Nome 2: ')
nome3 = input('Nome 3: ')

lista_alunos.append(nome1)
lista_alunos.append(nome2)
lista_alunos.append(nome3)

notas_aluno1 = [float(input(f'nota 1: {nome1} ')), float(input(f'nota 2: {nome1} ')) ]
notas_aluno2 = [float(input(f'nota 1: {nome2} ')), float(input(f'nota 2: {nome2} ')) ]
notas_aluno3 = [float(input(f'nota 1: {nome3} ')), float(input(f'nota 2: {nome3} ')) ]

media_aluno1 = sum(notas_aluno1)/len(notas_aluno1)
media_aluno2 = sum(notas_aluno2)/len(notas_aluno2)
media_aluno3 = sum(notas_aluno3)/len(notas_aluno3)

print('Média alunos')

print(f'''

Médias:
aluno: {nome1} - {media_aluno1}     
aluno: {nome2} - {media_aluno2}        
aluno: {nome3} - {media_aluno3}               
''')

aprovado_01 = media_aluno1 >= 7
aprovado_02 = media_aluno2 >= 7
aprovado_03 = media_aluno3 >= 7

print(f'''

{nome1} - APROVADO - {aprovado_01}
{nome2} - APROVADO - {aprovado_02}   
{nome3} - APROVADO - {aprovado_03}              
''')