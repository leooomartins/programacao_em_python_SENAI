import random

# exercicio 1
# n1 = int(input('Digite um número: '))

# if n1 > 0:
#     print('Esse número é positivo')
# elif n1 == 0:
#     print('Esse número é igual a zero')
# elif n1 < 0:
#     print('Esse número é negativo')

#exercicio 2
# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print('Você é maior de idade e faz parte do grupo que é obrigado a votar! ')
# elif idade >=16:
#     print('Você só vota se quiser! ')
# elif idade < 16:
#     print("Você não pode votar! ")

#exercicio 3
# variavel = random.randrange(1,20)
# print(variavel)

# if variavel == (2,20,2):
#     print('Número par')
# else: 
#     print('Número impar')

#exercicio 4
# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# n3 = int(input('Digite o terceiro número: '))

# if n1 == n2 == n3:
#     print('Você tem um triângulo Equilateiro: ')
# elif n1 == n2:
#     print('Você tem um triângulo isósceles') 
# elif n1 == n3:
#     print('Você tem um triângulo isósceles')
# elif n3 == n2:
#     print('Você tem um triângulo isósceles') 
# elif n2 == n3:
#     print('Você tem um triângulo isósceles') 
# elif n1 != n2 != n3:
#     print('Você tem um triângulo escaleno')

#exercício 5
# n1 = 5
# n2 = 7

# n3 = int(input('Indique um número: '))

# numero5 = n3 / n1
# numero7 = n3 / n2

# if numero5 == 5:
#     print('Esse número é múltiplo de 5: ', n3)
# elif numero7 == 7:
#     print('Esse número é múltiplo de 7: ', n3)

#exercicio 6
# n10 = int(input('Digite um número: '))

# if n10 > 10:
#     print('Esse número é positivo')
#     print('Esse número também é maior que 10')
# elif n10 <= 10:
#     print('Esse número é positivo, mas não é maior que 10')

#exercicio 7
n3 = int(input('Indique um numero: '))

resto_div_3 = n3 % 3
resto_div_5 = n3 % 5

if resto_div_3 == 0 and resto_div_5 == 0:
    print('Esse número é divisível por 3 e 5.')
elif resto_div_3 == 0:
    print('Esse número é divisível por 3.')
elif resto_div_5 == 0:
    print('Esse número é divisível por 5.')
else:
    print('Esse número não é divisível por 3 nem por 5.')