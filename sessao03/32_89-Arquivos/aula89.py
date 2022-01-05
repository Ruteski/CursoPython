# https://docs.python.org/3/library/functions.html#open

# file = open('abc.txt', 'w+')  # w+ modo leitura e escrita
# file.write('linha 1\n')
# file.write('linha 2\n')
# file.write('linha 3\n')
#
# file.seek(0,0)
# print(file.read())
# print('******************')
# file.seek(0,0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
#
# file.seek(0,0)
# print('******************')
# for linha in file.readlines():
#     print(linha, end='')
#
# file.seek(0,0)
# print('******************')
# for linha in file:
#     print(linha, end='')
#
# file.close()


# try:
#     file = open('abc.txt', 'w+')
#     file.write('linha')
#     file.seek(0,0)
#     print(file.read())
# finally:
#     file.close()

# maneira pythonica de trabalhar
# with open('abc.txt', 'w+') as file:
#     file.write('linha 1\n')
#     file.write('linha 2\n')
#     file.write('linha 3\n')
#
#     file.seek(0,0)
#     print(file.read())
#
#
# with open('abc.txt', 'r') as file:  # apenas leitura
#     print(file.read())

# with open('abc.txt', 'a+') as file:  # append e escrita
#     file.write('outra linha\n')
#     file.seek(0,0)
#     print(file.read())

# import os
# os.remove('abc.txt')  # apaga o arquivo


import json

d1 = {
    'pessoa 1': {
        'nome': 'lincoln',
        'idade': 38,
    },
    'pessoa 2': {
        'nome': 'maria',
        'idade': 25,
    },
}

# print(d1)
d1_json = json.dumps(d1, indent=True)
# print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
