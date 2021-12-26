nome = 'Lincoln'
idade = 38
altura = 1.74
e_maior = idade >= 18
peso = 88
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura', altura)
print('É maior de idade: ', e_maior)
print('Peso:', peso)
print('IMC:', imc)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

# utilizar f strings
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # o :.2f formata a saida do float para apenas 2 casas decimais

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

print('{0} {1} {2}  tem {1} {0} anos de idade e seu imc é {1} {2}'.format(nome, idade, imc))

print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))

