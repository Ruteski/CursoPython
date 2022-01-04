# lists, tuples, str -> sequences -> iteraveis
nome = 'lincoln ruteski'
iterador = iter(nome)
gerador = (letra for letra in nome)

try:
    print(next(iterador))  # l
    print(next(iterador))  # i
    print(next(iterador))  # n
    print(next(iterador))  # c
    print(next(iterador))  # o
    print(next(iterador))  # l
    print(next(iterador))  # n
    print(next(iterador))  #
    print(next(iterador))  # r
    print(next(iterador))  # u
    # print(next(iterador))  # t
    # print(next(iterador))  # e
    # print(next(iterador))  # s
    # print(next(iterador))  # k
    # print(next(iterador))  # i
except:
    pass

print('CADE OS VALORES')

for valor in iterador:
    print(valor)
