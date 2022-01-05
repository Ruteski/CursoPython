#        indices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    letra = frase[contador]

    if letra == 'r':
        nova_string += letra.upper()
    else:
        nova_string += letra
    # print(frase[contador], contador)
    # print(nova_string)
    contador += 1

print(nova_string)
