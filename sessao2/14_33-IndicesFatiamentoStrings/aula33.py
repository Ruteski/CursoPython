"""
Manipulando strings
* indice
* fatiamento [inicio:fim:passo]
* funcoes built-in len, abs, type, print, etc ...
Essas funcoes pomdem ser usadas diretamente em cada tipo

https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""

# indice
# positivos  [012345678]
texto =      'python s2'
# negativos -[987654321]

print(texto[2])
print(texto[-7])

# fatiamento
nova_string = texto
print(texto[2:6])
print(texto[:6])
print(texto[7:])
print(texto[-1])
print(texto[-9:-3])
print(texto[::2])
