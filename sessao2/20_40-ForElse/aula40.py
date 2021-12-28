
variavel = ['Lincoln', 'Marisa', 'Moises']
# star_with_m = False

# for valor in variavel:
#     if valor.lower().startswith('k'):
#         break
#     # if valor.startswith('m'):
#     #     print('começa com m', valor)
#     # else:
#     #     print('nao começa com m', valor)
#     #
#     # if valor.startswith('m'):
#     #     star_with_m = True
# else:
#     print('nao existe uma palavra que começa com J')

for valor in variavel:
    if valor.lower().startswith('m'):
        continue
    print(valor)
else:
    print('nao existe uma palavra que começa com j')
