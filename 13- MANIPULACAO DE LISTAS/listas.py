'''
Manipulação de listas é uma parte fundamental, pois as listas são estruturas de dados versáteis e amplamente utilizadas para armazenar coleções de elementos.

    Você pode criar uma lista simplesmente colocando elementos entre colchetes [].
'''
minha_lista = [1, 2, 3, 4, 5]


'''
Acessando elementos:

Você pode acessar elementos individuais de uma lista usando índices.'''
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista[0])  # Saída: 1


'''
Adicionando elementos:

Você pode adicionar elementos a uma lista usando os métodos append() para adicionar no final da lista, insert() para adicionar em uma posição específica ou a concatenação de listas usando o operador +.
'''
minha_lista = [1, 2, 3]
minha_lista.append(4)
minha_lista.insert(0, 0)
nova_lista = minha_lista + [5, 6]
print(minha_lista)  # Saída: [0, 1, 2, 3, 4]
print(nova_lista)   # Saída: [0, 1, 2, 3, 4, 5, 6]

'''
Removendo elementos:

Você pode remover elementos de uma lista usando os métodos remove() para remover um elemento específico, pop() para remover um elemento pelo índice ou del para remover um intervalo de elementos.
'''
minha_lista = [1, 2, 3, 4, 5]
minha_lista.remove(3)
valor_removido = minha_lista.pop(1)
del minha_lista[0]
print(minha_lista)     # Saída: [2, 4]
print(valor_removido)  # Saída: 2

'''
Verificando a existência de elementos:

Você pode verificar se um elemento está presente em uma lista usando o operador in.
'''
minha_lista = [1, 2, 3, 4, 5]
print(3 in minha_lista)  # Saída: True
print(6 in minha_lista)  # Saída: False

'''
Ordenando elementos:

Você pode ordenar os elementos de uma lista usando o método sort().
'''
minha_lista = [3, 1, 4, 1, 5, 9, 2]
minha_lista.sort()
print(minha_lista)  # Saída: [1, 1, 2, 3, 4, 5, 9]

'''Outras operações comuns:

    len(lista): Retorna o número de elementos na lista.
    lista.index(elemento): Retorna o índice da primeira ocorrência de elemento na lista.
    lista.count(elemento): Retorna o número de ocorrências de elemento na lista.
    lista.reverse(): Inverte a ordem dos elementos na lista.
'''