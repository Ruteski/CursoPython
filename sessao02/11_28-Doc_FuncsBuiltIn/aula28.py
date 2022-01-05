# https://docs.python.org/3/library/stdtypes.html

num1 = input('digite um numero: ')
num2 = input('digite outro numero: ')

# isnumeric isdigit isdecimal

# checa apenas numeros inteiros e positivos
# print(num1.isnumeric())
# print(num2.isnumeric())

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#
#     print(num1 + num2)
# else:
#     print('nao pude converter os numeros para realizer contas.')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')
