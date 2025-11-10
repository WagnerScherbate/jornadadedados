CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
name = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("informe seu Salrio: "))


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Informe o bonus recebido: "))


# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario * bonus

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"o Usuario {name} possui o bonus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?