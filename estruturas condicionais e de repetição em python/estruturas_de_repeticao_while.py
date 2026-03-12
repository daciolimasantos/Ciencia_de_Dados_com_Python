opcao = -1

while opcao != 0:
    opcao = int(input('[1] sacar \n[2] extrato \n[0] sair \n:'))

    if opcao == 1:
        print('sacando ...')
    elif opcao == 2:
        print('exibindo o extrato ...')
else:
    print('obrigado por investir conosco!')

#ESTRUTURA DE REPETIÇÃO BREAK - break encerra o looping sob determinada condição. --- o continue é o bypass sob condição específica, ele pula a condição.

while True:
    onumero = int(input('informe um número:'))

    if onumero == 10:
        break

    print(onumero)