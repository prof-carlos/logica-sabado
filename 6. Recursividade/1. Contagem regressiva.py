def contagem_regressiva(n):
    if n < 0:  # caso base
        return
    print(n)
    contagem_regressiva(n - 1)  # chamada recursiva

# Exemplo de uso
contagem_regressiva(5)
