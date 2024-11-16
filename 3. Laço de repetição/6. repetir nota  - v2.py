import os

os.system("cls || clear")

# Entrada
while True:
    nota = float(input("Digite uma nota: "))

    # Processamento
    if nota >= 0 and nota <= 10:
        # Saída
        print(f"Nota: {nota}")
        break
        
