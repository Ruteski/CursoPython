from random import randint

cpf = str(randint(100000000, 999999999))
cpf_sem_digito = cpf[:9]
total1 = 0
total2 = 0
digito1 = None
digito2 = None
calc = None

# calculo do primeiro digito
for indice, valor in enumerate(range(10, 1, -1)):
    total1 += int(cpf[indice]) * valor

calc = 11 - (total1 % 11)
if calc > 9:
    digito1 = 0
else:
    digito1 = calc


# calculo do segundo digito
for indice, valor in enumerate(range(11, 2, -1)):
    total2 += int(cpf[indice]) * valor

total2 += digito1 * 2
calc = 11 - (total2 % 11)
if calc > 9:
    digito2 = 0
else:
    digito2 = calc

# validacao
novo_cpf = cpf_sem_digito + str(digito1) + str(digito2)

print('CPF:', novo_cpf)

