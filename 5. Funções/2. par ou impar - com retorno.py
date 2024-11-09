import os

# Função sem retorno
def logo_senai():
    os.system("cls || clear")
    print("=== SENAI ===")

# Processamento
# Função com retorno
def par_impar(numero):
    if numero % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"

    return resultado

# Entrada de dados
logo_senai()
numero = int(input("Digite um número: "))

# Chamando a função
resposta = par_impar(numero)

logo_senai()
print(f"O númer: {numero} é {resposta}.")
