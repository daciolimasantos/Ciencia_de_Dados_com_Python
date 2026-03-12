# Leitura do numero de exportacoes
n = int(input())

# Inicializa o dicionario para armazenar toneladas por pais
exportacoes = {}

# Loop para ler os dados de cada exportacao
for _ in range(n):
    linha = input().strip()
    pais, toneladas = linha.split(",")
    pais = pais.strip()
    toneladas = float(toneladas.strip())
    
# Acumule as toneladas (uma linha só)
exportacoes[pais] = exportacoes.get(pais, 0) + toneladas

# Imprima o total de toneladas por pais
for pais, total in exportacoes.items():
    print(f"{pais}: {int(total) if total.is_integer() else total} toneladas")