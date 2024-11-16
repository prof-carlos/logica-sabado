import os

os.system("cls || clear")

""" Refatore:
    1 - Crie uma função para verificar se está aprovado.
        - Considere média maior ou igual a 7,0 para aprovação
        - Caso contrário, reprovado

    2 - Use uma lista para armazenar as notas.
"""

# Inicializando variáveis.
notas = [] # Lista
QUANTIDADE_NOTAS = 4

def calcular_media(notas, quantidade_notas):
    media = sum(notas) / quantidade_notas
    return media

def verificar_aprovacao(media):
    if media >= 7:
        resultado = "Aprovado!"
    else: 
        resultado = "Reprovado!"

    return resultado


# Entrada 
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

# Processamento
media = calcular_media(notas, QUANTIDADE_NOTAS)
resultado = verificar_aprovacao(media)

# Saída
print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")
