saldo = 2000
saque = 10000

status = 'sucesso' if saldo >= saque else 'falha'
print (f'{status} ao realizar o saque!')