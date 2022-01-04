"""
count -modulo itertools
"""
from itertools import count

# contador = count()
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))

# contador = count(start=5, step=0.05)
#
# for valor in contador:
#     print(round(valor, 2))
#
#     if valor >= 10:
#         break


contador = count()
lista = ['luiz', 'joao', 'maria']
lista = zip(contador, lista)
print(list(lista))
