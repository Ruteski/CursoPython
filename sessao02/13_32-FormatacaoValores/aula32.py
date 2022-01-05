"""
Formantando valores com modificadores - aula 5

:s - texto (strings)
:d - inteiros (int)
:f - numeors de ponto flutuante (float)
:.(NUMERO)f - quantidade de casas decimais (float)
:(CARACTERRE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

# num1 = 10
# num2 = 3
# divisao = num1 / num2
#
# # print( '{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')

num1 = 1
# numero com 10 digitos, complentando com zeros a esquerda
print(f'{num1:0>10}')

num2 = 359
# numero com 10 digitos, complentando com zeros a esquerda
print(f'{num2:0>10}')

num3 = 5842
# numero com 10 digitos, complentando com zeros a direita
print(f'{num3:0<10}')

num4 = 1874
# numero com 10 digitos, complentando com zeros e o numero no meio
print(f'{num4:0^10}')

num5 = 858
# transforma um int e float
print(f'{num5:.2f}')

num6 = 6178
# transforma um int e float, completa o numero com 10 digitos a esquerda
print(f'{num6:0>10.2f}')

nome = ' RUTESKI '
# coloca o nome no meio e preenche com # entre ele
print(f'{nome:#^20}')

nome = ' LINCOLN '
nome_formatado = '{:@>20}'.format(nome)
print(nome_formatado)

nome = 'Lincoln'
sobrenome = 'Ruteski'
nome_formatado = '{1:#^20}'.format(nome, sobrenome)
print(nome_formatado)


nome = 'Lincoln Ruteski'
nome = nome.ljust(20, '#')
print(nome)

nome = 'Lincoln Ruteski'
print(nome.lower())
print(nome.upper())
print(nome.title())
