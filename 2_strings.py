# Exibindo múltiplas linhas com print()
# O caractere especial \n é usado para quebrar a linha na impressão
print("line 1 \nline 2")

# Exibindo aspas duplas dentro de uma string
# Usamos a barra invertida \ para escapar as aspas duplas
print("example \"")

# Trabalhando com strings em Python
phrase = "phrase"

# Convertendo a string para maiúsculas
# A função upper() retorna uma nova string com todos os caracteres em maiúsculas
uppercase_phrase = phrase.upper()
print(uppercase_phrase)  # Saída: "PHRASE"

# Capitalizando a string (primeira letra em maiúscula, o restante em minúsculas)
# A função capitalize() retorna uma nova string com a primeira letra em maiúscula
capitalized_phrase = phrase.capitalize()
print(capitalized_phrase)  # Saída: "Phrase"

# Obtendo o comprimento da string
# A função len() retorna o número de caracteres na string
phrase_length = len(phrase)
print(phrase_length)  # Saída: 6

# Acessando um caractere específico da string pelo índice
# Lembrando que o índice em Python começa em 0
second_character = phrase[1]
print(second_character)  # Saída: "h"

# Encontrando o índice de um caractere específico na string
# A função index() retorna o índice da primeira ocorrência do caractere
index_of_p = phrase.index('p')
print(index_of_p)  # Saída: 0

# Substituindo uma substring por outra na string
# A função replace() retorna uma nova string com todas as ocorrências substituídas
replaced_phrase = phrase.replace("phrase", "frase")
print(replaced_phrase)  # Saída: "frase"
