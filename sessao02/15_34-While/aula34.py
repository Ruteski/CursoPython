# while True:
#     nome = input('Qual o seu nome? ')
#     print(f'Olá {nome}!')

# x = 0
# while x < 10:
#     if x == 3:
#         x += 1
#         # continue
#         break  # para a execucao do while
#
#     print(x)
#     x += 1
#
# print('acabou')

# x = 0  # coluna
#
# while x < 10:
#     y = 0  # linha
#
#     while y < 5:
#         print(f'({x},{y})')
#         y += 1
#
#     x += 1
#
# print('acabou')


while True:
    print()
    sair = input('deseja sair? [s]im ou [n]ão: ')

    if sair.lower() == 's':
        break

    num1 = input('digite um numero: ')
    num2 = input('digite outro numero: ')
    operador = input('digite um operador(+, -, *, /): ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('voce precisa digitar um numero ou sair')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('operador invalido')



