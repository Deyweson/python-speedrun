# Obtendo entrada do usuário

# Solicita ao usuário que insira seu nome
# A função input() exibe a mensagem e espera a entrada do usuário, armazenando o valor na variável 'name'
name = input("Enter your name: ")

# Exibindo uma saudação personalizada
# Usamos a função print() para exibir a mensagem no console
# O operador + é utilizado para concatenar strings
print("Hello, " + name + "!")

# Exemplos adicionais de obtenção de entrada do usuário

# Solicita ao usuário que insira sua idade
# Convertendo a entrada para um número inteiro usando a função int()
age = int(input("Enter your age: "))

# Calculando o ano de nascimento do usuário com base na idade fornecida
# Supondo que o ano atual seja 2024
current_year = 2024
birth_year = current_year - age

# Exibindo o ano de nascimento do usuário
print("You were born in " + str(birth_year) + ".")

# Usando formatação de strings para exibir mensagens
# A função format() ou f-strings (Python 3.6+) podem ser usadas para inserir variáveis em strings
print("Hello, {}! You are {} years old.".format(name, age))
print(f"Hello, {name}! You are {age} years old.")

# Solicitando e manipulando múltiplas entradas do usuário
# Obtendo o nome completo do usuário
full_name = input("Enter your full name: ")

# Dividindo o nome completo em uma lista de palavras
name_parts = full_name.split()

# Exibindo cada parte do nome em uma linha separada
print("Your name parts are:")
for part in name_parts:
    print(part)

# Solicitando e convertendo entrada para ponto flutuante
height = float(input("Enter your height in meters: "))

# Exibindo a altura formatada
print(f"Your height is {height:.2f} meters.")
