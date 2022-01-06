from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass


class B(A):
    def falar(self, msg):
        print(f'B esta falando {msg}')


class C(A):
    def falar(self, msg):
        print(f'C esta falando {msg}')


b = B()
c = C()

b.falar('hello')
c.falar('ahoiiii')
