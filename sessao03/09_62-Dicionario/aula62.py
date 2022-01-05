# d1 = {'chave1': 'valor da chave 1','chave2': 'valor da chave 2'}
# d1 = dict(chave1='valor da chave 1', chave2='valor da chave 2')
# d1['chave3'] = 'valor da chave 3'
#
# print(d1)

d1 = {
    'str': 'valor',
    123: 'outro valor',
    (1,3,2,4): 'tupla'
}

# print(d1[(1,3,2,4)])

# d1['chavenaoexiste'] = 'agora existe'
#
# if 'chavenaoexiste' in d1:
#     print(d1['chavenaoexiste'])
#
# print('oi')

# d1.update({'nova_chave':'novo_valor'})
#
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))
#
# print(d1.get(123))
#
# del d1['str']
#
# print(d1)

# print('str' in d1)
# print('valor' in d1.values())
# print(len(d1))

# for k in d1:
#     print(k)
#
# for v in d1.values():
#     print(v)

# for n in d1.items():
#     print(n)

# for k, v in d1.items():
#     print(k, v)

# clientes = {
#     'cliente1': {
#         'nome': 'lincoln',
#         'sobrenome': 'ruteski',
#     },
#     'cliente2': {
#         'nome': 'mary',
#         'sobrenome': 'doe',
#     },
#     'cliente3': {
#         'nome': 'jhon',
#         'sobrenome': 'doe',
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')
#


# d1 = {1: 'a', 2: 'b', 3:'c', 'd':['lincoln', 'ruteski']}
# # v = d1
# v = d1.copy()
#
# v[1] = 'ruteski'
#
# print(v['d'][1])
# print(d1)
# print(v)

# lista = [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
# ]
#
# d1 = dict(lista)
#
# print(d1)


d1 = {
    1: 2,
    3: 4,
    5: 6,
}

d2 = {
    'a': 'b',
    'c': 'd',
}

d1.update(d2)

# d1.pop(5)
print(d1)
