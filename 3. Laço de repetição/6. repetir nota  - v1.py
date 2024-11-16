import os

os.system("cls || clear")

# Entrada
while True:
    nota = float(input("Digite uma nota: "))

    # Processamento
    if nota < 0 or nota > 10:
        continue
    else:
        # Saída
        print(f"Nota: {nota}")
        break
    
