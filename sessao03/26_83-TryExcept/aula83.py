try:
    # a = 1/0
    a = 0
    try:
        a = 1/0
    except:
        print('deu ruim')
except NameError as erro:
    print('erro do desenvolvedor, fale com ele')
except (IndexError, KeyError) as erro:
    print('erro de indice ou chave')
except Exception as erro:
    print('ocorreu um erro inexperado: ', erro)
else:
    # print('seu codigo foi executado com sucesso')
    pass
finally:
    # print('finalizou')
    a = None

print(a)
