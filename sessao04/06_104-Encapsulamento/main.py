"""
public, protected, private

_ private/protected

__ private fortemente privado (_NOMECLASSE__nomeatributo)
"""


class BaseDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()
bd.inserir(1, 'lincoln')
bd.inserir(2, 'ruteski')
bd.inserir(3, 'maria')

# bd.__dados = 'outra coisa'
# bd.listar()
print(bd.dados)
