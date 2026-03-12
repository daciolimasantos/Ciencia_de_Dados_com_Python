#operadores lógicos
#and [e]; or[ou];

saldo = 1000
saque = 200
limite = 100

checa_valor = saldo >= saque and saque <= limite
print(checa_valor)

#operadores lógicos de negação
#not [não é]

contato_emergencia = []

not 1000 > 1500
not contato_emergencia
not 'saque 1500'
not ''

#parenteses
saldo_2 = 1000
saque_2  = 350
limite_2 = 300
conta_especial = True

conta_1 = saldo_2 >= saque_2 and saque_2 <= limite_2 or conta_especial and saldo_2 >= saque_2

#a conta a priorização e identeção é mais fácil de compreender
conta_2 = (saldo_2 >= saque_2 and saque_2 <= limite_2) or (conta_especial and saldo_2 >= saque_2)

print(conta_1, conta_2)