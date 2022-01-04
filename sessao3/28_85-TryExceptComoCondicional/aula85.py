def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as error:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um numero: '))

    if numero is not None:
        print(numero * 5)
    else:
        print('Erro: isso nao é um numero')

    print()
