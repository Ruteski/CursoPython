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
print('**********')

c2 = ClienteVIP('jorge', 57, 'almeida')
c2.falar()
