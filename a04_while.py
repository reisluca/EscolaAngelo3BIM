numero = int(input("Digite um número para ver a tabuada: "))

multiplicador = 1

while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador += 1