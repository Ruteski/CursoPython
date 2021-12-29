# string = 'o brasil é o pais do futebal, o brasil é penta.'
# lista1 = string.split(' ')
# lista2 = string.split(',')

# print(lista2)

# palavra = ''
# contagem = 0
#
# for valor in lista1:
#     # print(valor)
#     # print(f'a palavra "{valor}" apareceu {lista1.count(valor)}x na frase.')
#     qtd_vezes = lista1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'a palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')
#

# #### JOIN
# string = 'o brasil é penta.'
# lista = string.split(' ')
# string2 = ','.join(lista)
#
# print(string2)

# ### ENUMERATE
# string = 'o brasil é penta.'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

# lista = [
#     [1,2],
#     [3,4],
#     [5,6],
# ]
#
# for v in lista:
#     # print(v)
#     print(v[0], v[1])


# lista2 = [
#     [0,'lincoln'],
#     [1, 'joao'],
#     [2, 'maria'],
# ]
#
# for indice, nome in lista2:
#     print(indice, nome)

# lista = ['lincoln', 'joao', 'maria']

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# n1, n2, n3 = lista
#
# print(n2)


lista = [
    ['edu', 'joao', 'luiz'],
    ['maria', 'aline', 'joana'],
    ['helena', 'ed', 'lu'],
]

# enumerada = enumerate(lista)
# print(enumerada)
# print(list(enumerada))  # typecast

# enumerada = list(enumerate(lista))
# print(enumerada[0][1][2])

for v1, v2 in enumerate(lista):
    print(v1, v2)
