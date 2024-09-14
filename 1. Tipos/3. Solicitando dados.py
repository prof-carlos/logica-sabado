import os

os.system("cls || clear") #Limpa o terminal.

# Entrada.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite sua peso: "))

# Saída.
print("Nome: ", nome)
print(f"Idade: {idade}")

print("Nome: ", nome, " Idade: ", idade)
print(f"Nome: {nome} Idade: {idade}")