import os

os.system("cls || clear")

# Definindo o login e senha.
login_cadastrado = "marta"
senha_cadastrada = "123"
tentativas = 0

# Entrada
while True:
    login = input("\nDigite seu login: ")
    senha = input("Digite sua senha: ")
    tentativas += 1

    # Processamento
    if login == login_cadastrado and senha == senha_cadastrada:
        print("Acesso ao sistema!")
        break
    
    if tentativas >= 3:
        print("Permitido apenas 3 tentativas!")
        break


