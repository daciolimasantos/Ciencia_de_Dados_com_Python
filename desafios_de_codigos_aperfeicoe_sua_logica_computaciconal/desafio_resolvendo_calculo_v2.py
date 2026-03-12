while True:
    print("\n" + "="*40)
    print("NOVA INCLUSÃO DE DADOS")
    print("="*40)
    
    # Leitura dos dados de entrada
    peso = float(input("Digite o peso: "))
    preco_por_tonelada = float(input("Digite o preço por tonelada: "))
    tipo_cliente = input("Digite o tipo de cliente: ")

    clientes = {
        'novo cliente': {'desconto': 0.0},
        'cliente fidelizado': {'desconto': 0.05},
        'cliente premium': {'desconto': 0.10}
    }

    # Calcula o valor total sem desconto
    valor_total = peso * preco_por_tonelada

    # Aplica o desconto conforme o tipo de cliente
    if tipo_cliente in clientes:
        desconto = clientes[tipo_cliente]['desconto']
        
        # Mensagem apropriada para cada tipo
        if tipo_cliente == 'novo cliente':
            print("Tipo de cliente novo. Aplicando desconto padrão de 0%.")
        elif tipo_cliente == 'cliente fidelizado':
            print("Tipo de cliente fidelizado. Aplicando desconto de 5%.")
        elif tipo_cliente == 'cliente premium':
            print("Tipo de cliente premium. Aplicando desconto de 10%.")
        
        valor_final = valor_total * (1 - desconto)
    else:
        print("Tipo de cliente não cadastrado. Nenhum desconto aplicado.")
        valor_final = valor_total  # Sem desconto

    # Exibe o resultado formatado com duas casas decimais
    print(f"Valor final: R$ {valor_final:.2f}")
    
    # Menu de opções
    print("\n" + "-"*30)
    print("O que deseja fazer?")
    print("[1] - Fazer uma nova inclusão de dados")
    print("[2] - Encerrar o programa")
    print("-"*30)
    
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    if opcao == "2":
        print("\nPrograma encerrado. Obrigado por utilizar!")
        break
    elif opcao != "1":
        print("\nOpção inválida! Encerrando o programa por segurança.")
        break