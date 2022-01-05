# import vendas.calc_precos
# from vendas import calc_precos
from vendas.calc_precos import aumento, reducao
from vendas.formata.preco import real

preco = 49.9
# preco_aumento = vendas.calc_precos.aumento(preco, 5)
# preco_aumento = calc_precos.aumento(preco, 5)
preco_aumento = aumento(preco, 5)
print(real(preco_aumento))

preco = 49.9
preco_reducao = reducao(preco, 5, True)
print(preco_reducao)