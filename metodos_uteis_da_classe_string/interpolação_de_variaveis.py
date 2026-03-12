#esse método % não muito utilizado devido a sua complexidade.
# %s - string --- %d - inteiro

nome = 'Dacio Lima'
idade = 28
profissao = 'programador bilionario'
linguagem = 'Python e Solidity'

pessoa = {'nome': 'Dacio Lìma', 'idade': 38, 'profissao': ' programador bilionario', 'linguagem': 'python'}

print('olá, me chamo %s. eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' %(nome, idade, profissao, linguagem),'\n')

#metodo format padrão
print('olá, me chamo {}. eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem),'\n')

#metodo format por localização geográfica na lista.
print('olá, me chamo {1}. eu tenho {0} anos de idade, trabalho como {3} e estou matriculado no curso de {2}.'.format(idade, nome, linguagem, profissao),'\n')

#metodo format por definição de valor ele também é posisional
print('olá, me chamo {nome}. eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem),'\n')

#metodo format usando diiconário.
print('olá, me chamo {nome}. eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(**pessoa),'\n')

#metodo f-string
print(f'olá, me chamo {nome}. eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.','\n')

#formatando string com f-string
PI = 3.14159
print(f'valor de PI: {PI:.2f}')
print(f'valor de PI: {PI:10.2f}')