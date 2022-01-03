"""
add, update, clear, discard
union |
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estao nos dois sets, mas nao em ambos)
"""

# sets so recebem valores, não possuem chave e valor igual os dicionarios(json)
# sets nao respeitam ordem
# sets nao repetem valores

# s1 = {1,2,3,4,5,6}
# s2 = set()  # criar set vazio
# s2.add(1)
# s2.add(2)
# s2.add(3)
# s2.add(4)
# s2.add(5)
# s2.update('a')
# s2.update('python')
#
# s2.discard(2)
#
# for v in s2:
#     print(v)

# l1 = [1,2,1,1,3,4,5,5,6,6,6,6,6,7,8,9,'lincoln', 'lincoln']
# print(l1)
#
# l1 = set(l1)
# print(l1)
#
# l1 = list(l1)
# print(l1)

# s1 = {1,2,3,4,5, 7}
# s2 = {1,2,3,4,5,6}
# s3 = s1 | s2
# s4 = s1 & s2
# # s5 = s1 - s2
# s5 = s2 - s1
# s6 = s1 ^ s2
#
# print(s6)


l1 = ['lincoln', 'joao', 'maria']
l2 = ['lincoln', 'joao', 'maria','lincoln','lincoln','lincoln','lincoln','lincoln', 'maria']
print(l1 != l2)

l1 = set(l1)
l2 = set(l2)
print(l1 == l2)
