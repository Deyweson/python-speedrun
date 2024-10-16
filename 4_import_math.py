# Importando módulos externos

# Importando todas as funções do módulo math
# Isso permite que usemos funções matemáticas avançadas diretamente
from math import *

# Arredondamento para baixo
# A função floor() arredonda o número para o inteiro mais próximo menor ou igual a ele
print(floor(3.7))  # Saída: 3

# Arredondamento para cima
# A função ceil() arredonda o número para o inteiro mais próximo maior ou igual a ele
print(ceil(3.7))  # Saída: 4

# Raiz quadrada
# A função sqrt() retorna a raiz quadrada do número
print(sqrt(36))  # Saída: 6.0

# Exponenciação
# A função pow() retorna a base elevada ao expoente
print(pow(2, 3))  # Saída: 8 (2^3)

# Constantes matemáticas
# O módulo math também fornece constantes matemáticas úteis
print(pi)  # Saída: 3.141592653589793
print(e)   # Saída: 2.718281828459045

# Logaritmo
# A função log() retorna o logaritmo natural (base e) do número
print(log(10))  # Saída: 2.302585092994046

# Logaritmo com base 10
# A função log10() retorna o logaritmo na base 10 do número
print(log10(10))  # Saída: 1.0

# Valor absoluto
# A função fabs() retorna o valor absoluto do número (resultado é sempre um ponto flutuante)
print(fabs(-3.7))  # Saída: 3.7

# Seno, Cosseno e Tangente
# As funções sin(), cos() e tan() retornam, respectivamente, o seno, cosseno e tangente de um ângulo em radianos
print(sin(pi / 2))  # Saída: 1.0 (seno de 90 graus)
print(cos(0))       # Saída: 1.0 (cosseno de 0 graus)
print(tan(pi / 4))  # Saída: 1.0 (tangente de 45 graus)

# Convertendo graus para radianos e vice-versa
# A função radians() converte um ângulo de graus para radianos
# A função degrees() converte um ângulo de radianos para graus
angle_degrees = 180
angle_radians = radians(angle_degrees)
print(angle_radians)  # Saída: 3.141592653589793 (180 graus em radianos)
print(degrees(angle_radians))  # Saída: 180.0 (π radianos em graus)
