num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
diferenca = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "indefinido (divisão por zero)"

print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")