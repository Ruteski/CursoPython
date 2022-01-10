"""
Pilhas e Filas
Pilha(stack) - LIFO - last in, first out
Fila(queue) - FIFO - first in, first out

filas podem ter efeitos colaterais em desempenho, pq a cada item alterado, todos os indices serao modificados
"""

# PILHA
# livros = list()
#
# livros.append('livro 1')
# livros.append('livro 2')
# livros.append('livro 3')
# livros.append('livro 4')
# livros.append('livro 5')
# print(livros)
# livros_removidos = livros.pop()  # 5
# livros_removidos = livros.pop()  # 4
# livros_removidos = livros.pop()  # 3
# print(livros)
# print(livros_removidos)

# FILA
from collections import deque

# fila = deque(maxlen=5)
# fila.extend([1,2,3,4])
# print(fila)
# fila.extend(5)
# print(fila)
# fila.extend(6)
# print(fila)

# for i in range(1,1000):
#     fila.append(i)
#     sleep(1)
#     print(fila)



fila = deque()
fila.append('joaozinho')
fila.append('maria')
fila.append('jorge')
fila.append('lucas')
fila.append('ana')
fila.append('ester')
fila.append('lincoln')

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

print(fila)
