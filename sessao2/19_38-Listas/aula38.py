"""
listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1         2    3    4   5
lista = ['a', 'bacana', 'c', 'd', 'e', 10.5]
#   -     6    5         4    3    2   1

lista[4] = 'qualquer outra coisa'
#
# print(lista)
# print(lista[:3])
# print(lista[2:])
# print(lista[::2])
# print(lista[::-1])

# palindromo = 'socorram me subi no onibus em marrocos'
# print(palindromo[::-1])


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# l1.extend(l2)
# l1.extend('a')
# l2.append('b')

# print(l2)
# l2.insert(0, 'banana')
# print(l2)
# l2.pop()
# print(l2)

# print(l1)
# print(l2)
# print(l3)

# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l2)
# l2.insert(0, 'banana')
# print(l2)
# del(l2[0])
# print(l2)

# print(max(l2))
# print(min(l2))

# l2 = list(range(1, 10))
# print(l2)

# l2 = list(range(0, 100, 8))
# print(l2)

# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for valor in l2:
#     print(valor)

# l2 = ['String', True, 10, -20.5]
#
# for elem in l2:
#     print(f'o tipo de elem é {type(elem)} e seu valor é {elem}')


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('VOCÊ PERDEU')
        break

    letra = input('digita uma letra: ')

    if len(letra) > 1:
        print('digite apenas 1 letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'aeeeeee, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'a letra "{letra}" NAO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'VOCÊ GANHOU!!! A palavra secreta era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances')
