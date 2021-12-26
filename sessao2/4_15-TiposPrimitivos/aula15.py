"""
Tipos de dados
str - string - textos 'assim' ou "assim"
int - inteiro - 123 10 20 235486 -150
float - real/ponto flutuante - 10.56 956.63 89.846.95
bool - booelan/lógico - True/False (10 == 10)
"""
print('"ruteski"', type('ruteski'))
print(123456, type(123456))
print('"123456"', type('123456'))
print(12.5, type(12.5))
print('True', type(True))
print(10 == 10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))
print('l' == 'L', type('l' == 'L'))
print(bool(''))
print(bool([]))
print(bool(0))

# type cast
print('lincoln', type('lincoln'), bool('lincoln'))
print(int(12.6))
print('10', int('10'), type(int('10')))
print(str(15), type(str(15)))
print(str(15.6), type(str(15.6)))
print('15.6', float('15.6'), type(float(15.6)))
print('15', float('15'), type(float(15)))
print(10 + 10)
print('10' + '10')

# exercicio
# string: nome
print('Nome:', 'Lincoln Ruteski', ' - tipo:', type('Lincoln Ruteski'))

# int: idade
print('Idade:', 38, '- tipo:', type(38))

# float: altura
print('Altura:', 1.74, '- tipo:', type(1.74))

# booel: maior de idade?
print('Maior de idade:', 38 >= 18, '- tipo:', type(38 >= 18))

