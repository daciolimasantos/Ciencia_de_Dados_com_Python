def exibir_mensagem_0():
    print('hello motha fuckers!')

def exibir_mensagem_1(nome):
    print(f'seja bem vindo {nome}!') #aqui é obrigatorio passar o nome.

def exibir_mensagem_2(nome='Diana'):
    print(f'seja bem vindo {nome}!') #aqui a função já tem um argumento deafult.

print(exibir_mensagem_0())
print(exibir_mensagem_1('Davi'))
print(exibir_mensagem_2())
print(exibir_mensagem_2('Dante'))