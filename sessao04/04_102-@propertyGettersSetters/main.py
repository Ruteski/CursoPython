class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        self._nome = name.upper()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Produto('camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('caneca', 'R$15.25')
p2.desconto(11)
print(p2.nome, p2.preco)
