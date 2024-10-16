# Definindo Listas

# Definindo uma lista de amigos
friends = ["Kevin", "Karen", "Jim"]

# Imprimindo a lista completa
print("Lista de amigos:", friends)  # Saída: ['Kevin', 'Karen', 'Jim']

# Acessando elementos da lista por índice

# Imprimindo o primeiro elemento da lista (índice 0)
print("Primeiro amigo:", friends[0])  # Saída: Kevin

# Usando índices negativos para acessar elementos a partir do final da lista

# Imprimindo o último elemento da lista (índice -1)
print("Último amigo:", friends[-1])  # Saída: Jim

# Fatiando listas para acessar subconjuntos de elementos

# Pegando todos os elementos a partir do índice 1 até o final
print("Amigos a partir do segundo:", friends[1:])  # Saída: ['Karen', 'Jim']

# Pegando os elementos no intervalo do índice 1 ao 3 (exclusivo)
print("Amigos do segundo ao terceiro:", friends[1:3])  # Saída: ['Karen', 'Jim']

# Modificando elementos da lista

# Alterando o valor do elemento na posição 1
friends[1] = "Mike"
print("Lista após alteração:", friends)  # Saída: ['Kevin', 'Mike', 'Jim']