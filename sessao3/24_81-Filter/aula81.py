from dados import pessoas, lista, produtos

# nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5]
# for n in nova_lista:
#     print(n)

# nova_lista = filter(lambda p: p['preco'] > 50, produtos)
# for n in nova_lista:
#     print(n)


# def filtra(produto):
#     if produto['preco'] > 50:
#         return True
#     else:
#         return False
#
# nova_lista = filter(filtra, produtos)
# for n in nova_lista:
#     print(n)


def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)
for n in nova_lista:
    print(n)