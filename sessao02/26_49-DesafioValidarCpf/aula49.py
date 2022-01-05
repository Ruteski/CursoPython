"""
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

# for p, r in enumerate(range(10,1,-1)):
#     print(p, r)

# DESAFIO

"""
CPF = 168.995.350-09
-------------------------------
1 * 10 = 10           # 1 * 11 = 11
6 * 9 = 54            # 6 * 10 = 60
8 * 8 = 64            # 8 * 9 = 72
9 * 7 = 63            # 9 * 8 = 72
9 * 6 = 54            # 9 * 7 = 63
5 * 5 = 25            # 5 * 6 = 30
3 * 4 = 12            # 3 * 5 = 15
5 * 3 = 15            # 5 * 4 = 20
0 * 2 = 0             # 0 * 3 = 0
----------            # 0 * 2 = 0  --> esse zero é o digito 1 calculado anteriormente
                      # -----------------
soma  = 297           # soma   = 343
                      # 
11 - (297 % 11) = 11  # 11 - (343 % 11) = 9
11 > 9 = 0            # 9 > 9 = 9
Digito 1 = 0          # Digito 2 = 9
"""

cpf = input('Digite o cpf: ')
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
cpf_validacao = cpf_sem_digito + str(digito1) + str(digito2)

if cpf_validacao == cpf:
    print('CPF válido')
else:
    print('CPF inválido')


"""
#### RESOLUCAO DO PROFESSOR

while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')
"""