"""
funcoes - *args e **kwargs
"""

# def func(a1,a2,a3,a4,a5, nome=None, a6=None):
#     print(a1,a2,a3,a4,a5,nome, a6)
#     return nome, a6
#
#
# var = func(1,2,3,4,5, nome='lincoln', a6='5')
# print(var[0], var[1])

# **kwargs = key word args - argumentos nomeados, basicamente um json
def func(*args, **kwargs):
    # print(args)
    # print(args[0])
    # print(args[-1])  # acessa o ultimo item da lista
    # print(len(args))
    # for v in args:
    #     print(v)
    # print(args[0])
    print(args)
    print(kwargs)
    # print(kwargs['nome'])
    # print(kwargs['sobrenome'])
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('idade nao existe')

# lista = [1,2,3,4,5]
# n1, n2, *n = lista
# print(n1, n2, n)
# print(*lista, sep='\n')


# func(1,2,3,4,5,6)
lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='lincoln', sobrenome='ruteski')
