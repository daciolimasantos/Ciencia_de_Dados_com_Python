#estrutura de repetição for

texto = input('informe uma palavra: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

else:
    print()
    print('executando o final do laço.')