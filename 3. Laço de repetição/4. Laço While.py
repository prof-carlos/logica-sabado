import os

os.system("cls || clear")

# Enquanto for verdade.
while True:
    resposta = input("Digite uma resposta: ")

    # Aceita somente notas positivas.
    if resposta == "sim":
        break
    
    print("Digite novamente.")

print(f"Nota: {resposta}")
