# Leitura dos dados de entrada
peso = 10
preco_por_tonelada = 500
tipo_cliente = 'novo cliente'

# Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada

# TODO Aplique o desconto conforme o tipo de cliente
desconto = 0.0
if tipo_cliente == 'novo cliente':
    desconto = 0.0
elif tipo_cliente == 'cliente fidelizado':
    desconto = 0.05
elif tipo_cliente == 'cliente premium':
    desconto = 0.10
valor_final = valor_total * (1 - desconto)

# Exibe o resultado formatado com duas casas decimais
print(f"{valor_final:.2f}")