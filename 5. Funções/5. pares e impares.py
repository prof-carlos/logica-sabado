import os

os.system("cls || clear")

# Refatore este código para uso com uma função.

# Criando função.
def pares_impares():
    for i in range(1, 16):
        if i % 2 == 1:
            print(i)

# Chamada da função.
pares_impares()