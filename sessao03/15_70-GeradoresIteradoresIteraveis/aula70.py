# lista = [0,1,2,3,4,5]
# lista = iter(lista)  # transforma um item em interador
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
#
# print(hasattr(lista, '__iter__'))  # verifica se o item é iteravel
# print(hasattr(lista, '__next__'))  # verifica se o item é um iterador
#

import sys
import time

# lista = list(range(100))
# print(sys.getsizeof(lista))


# def gera():
#     # r = []
#     for n in range(100):
#         # r.append(n)
#         yield n
#         time.sleep(0.1)
#     # return r
#
#
# g = gera()
#
# for v in g:
#     print(v)



# def gera():
#     variavel = 'valor 1'
#     yield variavel
#     variavel = 'valor 2'
#     yield variavel
#     variavel = 'valor 3'
#     yield variavel
#
# g = gera()
#
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for v in g:
#     print(v)


l1 = [x for x in range(10000)]
print(type(l1))
print(sys.getsizeof(l1))

l2 = (x for x in range(10000))
print(type(l2))
print(sys.getsizeof(l2))

# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
print()
for v in l2:
    print(v)
    