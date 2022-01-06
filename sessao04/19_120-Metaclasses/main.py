"""
em python tudo é um objeto: incluindo classes
metaclasses sao as "classes" que criam as classes
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            # print(f'vc precisa criar o metodo b_fala em {name}')
            pass
        else:
            if not callable(namespace['b_fala']):
                # print(f'b_fala precisa ser um metodo, nao um atributo em {name}')
                pass


        # print(namespace)
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    # def fala(self):
    #     self.b_fala()
    attr_classe = 'valor a'


class B(A):
    # teste = 'valor'
    #
    # def b_fala(self):
    #     print('oi')
    #
    # def seila(self):
    #     pass
    attr_classe = 'valor b'


b = B()
print(b.attr_classe)
