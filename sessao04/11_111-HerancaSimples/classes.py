class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} falando ...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} comprando ...')

    def falar(self):
        print('Estou em CLIENTE')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} estudando ...')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        # super().__init__(nome, idade)
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        super().falar()  # no caso a classe cliente
        print(f'{self.nome} {self.sobrenome} falando ...')
