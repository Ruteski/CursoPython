"""
escopo
"""

variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel
    variavel = 'outro valor'
    print(variavel)


def func3():
    print(variavel)


func()
func2()
func3()
