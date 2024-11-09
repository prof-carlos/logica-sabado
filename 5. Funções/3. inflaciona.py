import os

# Função sem retorno
def logo_senai():
    os.system("cls || clear")
    print("=== SENAI ===")

def inflacionar_produto(valor_produto):
    if valor_produto < 100:
        inflaciona = valor_produto * 1.1
    else:
        inflaciona = valor_produto * 1.2
    
    return inflaciona

# Entrada
logo_senai()
valor_produto = float(input("Digite o valor do produto: "))

# Processamento
valor_inflacionado = inflacionar_produto(valor_produto)

# Saída
print(f"O produto com valor {valor_produto} inflacionado custa: {round(valor_inflacionado, 2)}")