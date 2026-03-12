conta_normal = True
conta_universitaria = False

saldo = 50000
saque = 60000
cheque_especial = 10000


if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso.')
    elif saque <= (saldo + cheque_especial):
        print('saque realizado com uso do cheque especial')
    else:
        print('não possivel realizar o saque, saldo insuficiente')
    
elif conta_universitaria:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    else:
        print('saldo insuficiente')
else:
    print('sisteman não reconhece o tipo de conta entre em contato com o seu gerente.')

''' 
MAIOR_IDADE = 18
MAIOR_IDADE_2 = 18
IDADE_ESPECIAL = 16

idade = int(input('informe sua idade: '))
idade_2 = int(input('informe sua idade: '))
idade_3 = int(input('informe sua idade: '))

#somente if

if idade >= MAIOR_IDADE:
    print('maior de idade, pode tirar a CNH. Paranbens, boa sorte e FO DA -SE!')

if idade < MAIOR_IDADE:
    print('ainda não pode tirar a CNH seu Fedelho!')

#com if e else

if idade_2 >= MAIOR_IDADE_2:
    print('maior de idade, pode tirar a CNH. Paranbens, boa sorte e FO DA -SE!')

else:
    print('ainda não pode tirar a CNH seu Fedelho!')

#com elif

if idade_3 >= MAIOR_IDADE_2:
    print('maior de idade, pode tirar a CNH. Paranbens, boa sorte e FO DA -SE!')

elif idade >= IDADE_ESPECIAL:
    print('ah apressadinho pode fazer as aulas teóricas somente. FDP!')

else:
    print('ainda não pode tirar a CNH seu Fedelho!')

'''