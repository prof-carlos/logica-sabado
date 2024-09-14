import os 

os.system("cls || clear")

resultado = 0

# Entrada.
primeiro_numero = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada (+ - / * ): ")
segundo_numero = float(input("Digite o segundo número: "))

# Processamento.
match operacao:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção inválida.")

# Saída.
print(f"Resultado: {resultado}")