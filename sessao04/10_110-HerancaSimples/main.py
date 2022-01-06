"""
associacao - usa
agregacao  - tem
composicao - é dono
herança    - é
"""
from classes import *

c1 = Cliente('lincoln', 38)
# print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('roger', 12)
# print(a1.nome)
a1.falar()
a1.estudar()

p1 = Pessoa('joao', 57)
p1.falar()
