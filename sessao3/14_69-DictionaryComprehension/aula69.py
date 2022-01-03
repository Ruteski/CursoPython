# lista = [
#     ('chave', 2),
#     ('chave1', 'valor1'),
# ]
#
# d1 = {x.upper(): y*2 for x, y in lista}
# d1 = dict(lista)
# print(d1)

# d1 = {x: y*2 for x, y in enumerate(range(5))}
# print(d1)

# d1 = {x for x in range(5)}
# print(d1)

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)
