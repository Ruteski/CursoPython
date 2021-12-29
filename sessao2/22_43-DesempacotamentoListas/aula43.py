lista = ['luis', 'joao', 'maria', 1,2,3,4,5,6,7,8,9,100]

# n1, n2, n3, *outra_lista, ultimo_da_lista = lista
# n1, n2, *_ = lista  # informa que vai usar apenas as 2 primeiras posicoes da lista, o resto nao importa
*outra_lista, n1, n2, n3 = lista

# print(n1, n2, n3, outra_lista, ultimo_da_lista)
print(outra_lista)
