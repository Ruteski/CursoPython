
def saudacao(msg='Olá', nome='usuario'):
    nome = nome.replace('a', '@')
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao('Hello', 'Lincoln')
saudacao()
saudacao(nome='Jao')
saudacao(nome='Maria', msg='Hi')

