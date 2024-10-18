# Comparações em Python

# Definindo uma função que retorna o maior de três números
def max_num(num1, num2, num3):
    # Usando comparações para determinar o maior número
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Chamando a função e imprimindo o resultado
print(max_num(3, 4, 5))