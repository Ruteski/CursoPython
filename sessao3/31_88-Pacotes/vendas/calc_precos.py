from vendas.formata.preco import real


def aumento(v, p, formata=False):
    r = v + (v * (p/100))

    if formata:
        return real(r)
    else:
        return r


def reducao(v, p, formata=False):
    r = v - (v * (p / 100))

    if formata:
        return real(r)
    else:
        return r
