"""
iniciar com letra, pode conter nuemros, separar _ , letras minusculas
"""

nome = 'Lincoln'
# print(nome, type(nome))
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
