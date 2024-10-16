# Listas de números da sorte e amigos
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar"]

# Estendendo a lista de amigos com os números da sorte
# O método extend() adiciona todos os elementos da lista passada como argumento ao final da lista original
friends.extend(lucky_numbers)
print("Após extend:", friends)  # Saída: ['Kevin', 'Karen', 'Jim', 'Oscar', 4, 8, 15, 16, 23, 42]

# Adicionando um novo amigo ao final da lista
# O método append() adiciona um único elemento ao final da lista
friends.append("Creed")
print("Após append:", friends)  # Saída: ['Kevin', 'Karen', 'Jim', 'Oscar', 4, 8, 15, 16, 23, 42, 'Creed']

# Inserindo um amigo em uma posição específica
# O método insert() insere um elemento na posição especificada, deslocando os elementos seguintes
friends.insert(1, "Kelly")
print("Após insert:", friends)  # Saída: ['Kevin', 'Kelly', 'Karen', 'Jim', 'Oscar', 4, 8, 15, 16, 23, 42, 'Creed']

# Removendo um amigo específico da lista
# O método remove() remove a primeira ocorrência do elemento especificado
friends.remove("Jim")
print("Após remove:", friends)  # Saída: ['Kevin', 'Kelly', 'Karen', 'Oscar', 4, 8, 15, 16, 23, 42, 'Creed']

# Limpando todos os elementos da lista de amigos
# O método clear() remove todos os elementos da lista, tornando-a vazia
friends.clear()
print("Após clear:", friends)  # Saída: []

# Adicionando elementos novamente para os próximos exemplos
friends = ["Kevin", "Karen", "Oscar", "Creed"]

# Removendo o último elemento da lista
# O método pop() remove e retorna o último elemento da lista
removed_friend = friends.pop()
print("Após pop:", friends)  # Saída: ['Kevin', 'Karen', 'Oscar']
print("Elemento removido:", removed_friend)  # Saída: Creed

# Obtendo o índice de um elemento na lista
# O método index() retorna o índice da primeira ocorrência do elemento especificado
kevin_index = friends.index("Kevin")
print("Índice de Kevin:", kevin_index)  # Saída: 0

# Contando a ocorrência de um elemento na lista
# O método count() retorna o número de vezes que o elemento especificado aparece na lista
jim_count = friends.count("Jim")
print("Quantidade de Jim na lista:", jim_count)  # Saída: 0

# Ordenando a lista de amigos em ordem alfabética
# O método sort() ordena a lista em ordem crescente (alfabética para strings)
friends.sort()
print("Amigos ordenados:", friends)  # Saída: ['Karen', 'Kevin', 'Oscar']

# Ordenando a lista de números da sorte em ordem crescente
lucky_numbers.sort()
print("Números da sorte ordenados:", lucky_numbers)  # Saída: [4, 8, 15, 16, 23, 42]

# Revertendo a ordem da lista de números da sorte
# O método reverse() inverte a ordem dos elementos na lista
lucky_numbers.reverse()
print("Números da sorte em ordem reversa:", lucky_numbers)  # Saída: [42, 23, 16, 15, 8, 4]

# Copiando a lista de amigos para uma nova lista
# O método copy() cria uma cópia superficial da lista
friends2 = friends.copy()
print("Cópia da lista de amigos:", friends2)  # Saída: ['Karen', 'Kevin', 'Oscar']
