"""
funções anonimas ou funcoes lambdas
"""

# forma de funcao
def funcao(arg1, arg2):
    return arg1*arg2


var = funcao(2,2)
# print(var)


# forma lambda
a = lambda x, y: x * y
# print(a(2,5))

lista = [
    ['p1', 12],
    ['p2', 2],
    ['p3', 1],
    ['p4', 22],
    ['p5', 14],
    ['p6', 50],
]

# def func(item):
#     return item[1]
#
#
# print(lista)
#
# lista.sort(key=func)
#
# print(lista)

lista.sort(key=lambda item: item[1], reverse=True)

print(lista)

print(sorted(lista, key=lambda i: i[1]))
