# Trabalhando com números em Python

# Imprimindo um número inteiro
print(10)  # Saída: 10

# Imprimindo um número decimal (ponto flutuante)
print(10.10)  # Saída: 10.1

# Operações aritméticas básicas
print(10 + 10)  # Adição, Saída: 20
print(10 - 10)  # Subtração, Saída: 0
print(10 / 10)  # Divisão, Saída: 1.0
print(10 * 10)  # Multiplicação, Saída: 100

# Definindo a ordem das operações usando parênteses
# A expressão dentro dos parênteses é avaliada primeiro
print((10 * 10) / 10)  # Saída: 10.0

# Operador módulo (%)
# Retorna o resto da divisão do primeiro número pelo segundo
print(10 % 3)  # Saída: 1

# Trabalhando com variáveis numéricas
my_num = 10

# Convertendo o número para uma string
# Isso é útil quando você deseja concatenar números com strings
print(str(my_num))  # Saída: "10"

# Funções matemáticas úteis

# Valor absoluto
# Retorna o valor absoluto do número (distância do zero)
print(abs(my_num))  # Saída: 10

# Potenciação
# pow(base, expoente) retorna o valor da base elevada ao expoente
print(pow(3, 2))  # Saída: 9 (3^2)

# Valor máximo
# Retorna o maior valor entre os argumentos fornecidos
print(max(3, 2))  # Saída: 3

# Valor mínimo
# Retorna o menor valor entre os argumentos fornecidos
print(min(3, 2))  # Saída: 2

# Arredondamento
# round(numero) arredonda o número para o inteiro mais próximo
print(round(3.7))  # Saída: 4

# Exemplos adicionais

# Divisão inteira
# // retorna o quociente inteiro da divisão
print(10 // 3)  # Saída: 3

# Exponenciação usando o operador **
# Retorna a base elevada ao expoente
print(3 ** 2)  # Saída: 9 (3^2)

# Arredondamento com precisão
# round(numero, n) arredonda o número para n casas decimais
print(round(3.14159, 2))  # Saída: 3.14
