#Estruturas Condicionais Simples

numero1 = 2
numero2 = 3

soma = 1000

if soma > 0:
    print('a soma é maior que zero.')
else:
    print('a soma é inferior a zero.') 

if numero1 == numero2:
    print('os números são iguais.')
else:
    print('os números são diferentes.')

#Estruturas Condicionais Compostas

if soma > 0:
    print('a soma é maior que zero.')
elif soma == 0:
    print('a soma é igual a zero.')
else:
    print('a soma é inferior a zero.')
    
#Esruturas Condicionais Aninhadas

idade = 20
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir")
    else:
        print("Sem carteira")
else:
    print("Menor de idade")