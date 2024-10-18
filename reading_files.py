# Lendo arquivos em Python

# Abrindo o arquivo 'matriz1.txt' em modo de leitura ('r')
file = open('file.txt', 'r')
# Lendo todas as linhas do arquivo e armazenando em uma lista
line = file.readlines()
print(line)  # Imprime a lista de linhas

# Movendo o cursor para o início do arquivo
file.seek(0)

# Lendo todo o conteúdo do arquivo como uma string única
content = file.read()
print(content)  # Imprime o conteúdo completo do arquivo

# Movendo o cursor para o início do arquivo novamente
file.seek(0)

# Lendo a primeira linha do arquivo
first_line = file.readline()
print(first_line)  # Imprime a primeira linha do arquivo