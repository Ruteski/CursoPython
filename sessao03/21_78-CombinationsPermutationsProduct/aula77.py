"""
combinations, permutations e product - modulo itertools
combinacao - ordem nao importa
permutacao - ordem importa
ambos nao repetem valores unicos
produto - ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product

pessoas = ['luiz', 'andre', 'eduardo', 'leticia', 'fabricio', 'rose']

for grupo in combinations(pessoas, 2):
    print(grupo)

print('\n#####################\n')

for grupo in permutations(pessoas, 2):
    print(grupo)

print('\n#####################\n')

for grupo in product(pessoas, repeat=2):
    print(grupo)