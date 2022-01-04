from dados import produtos, pessoas, lista

# nova_lista = map(lambda x: x*2, lista)
# nova_lista = [x*2 for x in lista]
# print(list(nova_lista))

# for produto in produtos:
#     print(produto)

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
#
# # precos = map(lambda p: p['preco'], produtos)
# novos_produtos = map(aumenta_preco, produtos)
# for produto in novos_produtos:
#     print(produto)


# nomes = map(lambda x: x['nome'], pessoas)
# for pessoa in nomes:
#     print(pessoa)


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)