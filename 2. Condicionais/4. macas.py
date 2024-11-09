import os
os.system("cls || clear")

# Entrada
quatidade_macas = int(input("Digite a quantidade de maçãs: "))

# Processamento
if quatidade_macas < 12:
    preco_final = quatidade_macas * 1.30
else:
    preco_final = quatidade_macas * 1

# Saída
print(f"Preço fina: {preco_final}")