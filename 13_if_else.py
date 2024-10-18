# If e Else em Python

# Variáveis booleanas
is_male = True
is_tall = True

# Usando 'if', 'elif' e 'else' para controle de fluxo com condições
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not is_tall:
    print("You are a short male.")
elif not is_male and is_tall:
    print("You are tall but not male.")
else:
    print("You are neither male nor tall.")

# Explicação detalhada:

# 1. 'if' Statement:
#    - A instrução 'if' executa um bloco de código se a condição for verdadeira.
#    - No exemplo, 'if is_male and is_tall:' verifica se as duas condições são verdadeiras.
#    - Se ambas forem verdadeiras, imprime "You are a tall male."

# 2. 'elif' Statement:
#    - A instrução 'elif' (abreviação de "else if") fornece condições adicionais.
#    - Ela é avaliada se a condição anterior (no caso, a instrução 'if') for falsa.
#    - O código no bloco 'elif' é executado se sua condição for verdadeira.
#    - No exemplo, 'elif is_male and not is_tall:' verifica se a pessoa é do sexo masculino, mas não é alta.
#    - 'elif not is_male and is_tall:' verifica se a pessoa não é do sexo masculino, mas é alta.

# 3. 'else' Statement:
#    - A instrução 'else' é executada se todas as condições anteriores forem falsas.
#    - No exemplo, o 'else' imprime "You are neither male nor tall" se nenhuma das condições anteriores for verdadeira.

# Exemplificando o uso do operador 'or':
if is_male or is_tall:
    print("You are male or tall or both.")
else:
    print("You are neither male nor tall.")

# Explicação do uso do 'or':
# - O operador 'or' retorna True se pelo menos uma das condições for verdadeira.
# - No exemplo, 'if is_male or is_tall:' verifica se a pessoa é do sexo masculino ou alta (ou ambas).
# - Se qualquer uma das condições for verdadeira, imprime "You are male or tall or both."
# - Caso contrário, imprime "You are neither male nor tall."

# Exemplificando o uso do operador 'and':
if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall.")

# Explicação do uso do 'and':
# - O operador 'and' retorna True se ambas as condições forem verdadeiras.
# - No exemplo, 'if is_male and is_tall:' verifica se a pessoa é do sexo masculino e alta.
# - Se ambas as condições forem verdadeiras, imprime "You are a tall male."
# - Caso contrário, imprime "You are either not male or not tall."
