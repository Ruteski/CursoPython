"""
for in
iterando strings com for
funcao range(start=0, stop, step=1)
"""
texto = 'python'
nova_string = ''
# for letra in texto:
#     print(letra)

# for n, letra in enumerate(texto):
#     print(n, letra)

# for n in range(10):
#     print(n)

# for n in range(0, 25, 3):
#     print(n)

# for n in range(20, 10, -1):
#     print(n)

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        # break
    else:
        nova_string += letra

print(nova_string)
