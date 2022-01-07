from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays
from calendar import monthrange


setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
ultimo_dia_mes = mdays[mes_atual]

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)

# ultimo dia do mes
print(mes_atual, mdays[mes_atual])

# ultimo dia mes ano bissexto
# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2020, 2))

# Saída - (5, 29)
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês

