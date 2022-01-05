from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return

        if self.falando:
            print(f'{self.nome} nao pode comer falando')
            return

        self.comendo = True
        print(f'{self.nome} esta comendo {alimento}')

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} nao esta comendo')
            return

        self.comendo = False
        print(f'{self.nome} parou de comer')

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} ja esta falando')
            return

        self.falando = True
        print(f'{self.nome} esta falando sobre {assunto}')

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao esta falando')
            return

        self.falando = False
        print(f'{self.nome} parou de falar')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
