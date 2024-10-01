idade = int(input("Digite a sua idade: "))

if 0 <= idade <= 12:
    print("Você é uma criança.")
elif 13 <= idade <= 17:
    print("Você é um adolescente.")
elif 18 <= idade <= 64:
    print("Você é um adulto.")
elif idade >= 65:
    print("Você é um idoso.")
else:
    print("Idade inválida.")