# https://docs.python.org/3/library/exceptions.html

# def divide(n1,n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as erro:
#         print('log:', erro)
#         raise
#
# try:
#     print(divide(2,0))
# except ZeroDivisionError as error:
#     print('erro: ', error)


def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 nao pode ser 0.')

    return n1/n2

try:
    print(divide(2,0))
except Exception as error:
    print(error)




