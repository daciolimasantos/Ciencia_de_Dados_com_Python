#versão apenas o if
saldo = 2000.0
saque = float(input('informe o valor do saque: R$ '))

if saldo >= saque:
    print ('realizando saque!')

if saldo < saque:
    print('saldo insuficiente!')

#versão if else
saldo = 2000.0
saque = float(input('informe o valor do saque: R$ '))

if saldo >= saque:
    print ('realizando saque!')

else:
    print('saldo insuficiente! seu pobre.')


#versão elif
opcao = int(input('informe uma opção: [1] sacar \n [2] extrato: '))

if opcao == 1:
    valor = float(input('informe a quantia para o saque: '))

elif opcao == 2:
    print('exibindo o extrato...')
else:
    
    SystemExit
    print ('opção inválida.')