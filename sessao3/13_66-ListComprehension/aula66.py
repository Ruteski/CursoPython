"""
otimizacao, performance
escrever menos codigo
"""

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['lincoln', 'joao', 'maria']
ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
# ex7 = [v if v % 3 == 0 else 'Não é' for v in l3]
ex7 = [v if v % 3 == 0 else f'{v} - não é' for v in l3]

ex8 = [v if v % 3 == 0 and v % 8 == 0 else f'{v} - não é' for v in l3]

# print(ex8)

"""
exercicio
string = '012345678901234567890123456789012345678901234567890123456789'
"""

string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i + n) for i in range(0, len(string), n)]
lista = [string[i:i+n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)

print(contadores)
print(tuplas)
print(lista)
print(retorno)
