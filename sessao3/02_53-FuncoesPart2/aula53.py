# def funcao(var):
#     # pass
#     return var
#
#
# variavel = funcao("Valor que eu quero")
#
# if variavel:
#     print(variavel)
# else:
#     print('nenhum valor')

# def divisao(n1, n2):
#     if n2 == 0:
#         return

#     return n1/n2

# divide = divisao(8,0)

# if divide:
#     print(divide)
# else:
#     print('conta invalida')

def f(var):
    print(var)


def dumb():
    return f


# var = dumb()('e colocar meu valor aqui')
var = dumb()
# print(id(var), id(f))

# if var == f:
#     print('var é igual a f')
# else:
#     print('blaaaaaa')

var('pode imprimir algo na tela')
