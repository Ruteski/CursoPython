"""
zip - unindo iteraveis
zip_longest - modulo itertools
"""

# codigo
cidades = ['curitiba', 'salvador', 'cuiaba', 'londrina', 'guarapuava']

# mais codigo
estados = ['pr', 'ba', 'mt']

cidades_estados = zip(estados, cidades)
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

# for valor in cidades_estados:
#     print(valor)
#     print(valor[0], valor[1])

# print(cidades_estados)
# print(dict(cidades_estados))

from itertools import zip_longest, count

indice = count()
# cidades_estados = zip_longest(estados, cidades)
cidades_estados = zip(
    indice,
    estados,
    cidades,
    
)

# print(list(cidades_estados))

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)


