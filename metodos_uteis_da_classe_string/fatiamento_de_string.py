#é utilizado como retorno/request de partes da string original - metodos start, stop, step

nome = 'Dacio Lima Santos Junior'

#fatiamento
print('1',nome[0],'\n') #primeira string.
print('2',nome[:9],'\n') #ele vai do 0 até o 8 ele não mostra o 9.
print('3',nome[10:],'\n') #a patir daqui até o final.
print('4',nome[7:12],'\n') #entre x e y.
print('5',nome[2:20:2],'\n') #aqui entre x e y, com o step/de dois em dois no caso.
print('6',nome[:],'\n') #não passa nada, ele retorna a cópia.
print('7',nome[::-1],'\n') #espelhamento de string