'''
Tuplas são estruturas de dados semelhantes a listas, mas com a diferença fundamental de serem imutáveis, ou seja, uma vez que uma tupla é criada, seus elementos não podem ser alterados, as tuplas são úteis para representar dados que não devem ser alterados, como coordenadas, configurações fixas e chaves de dicionário. 
'''

    # Criação de uma tupla:
tupla = (1, 2, 3, 4, 5)

    # Acessando elementos de uma tupla:
print(tupla[0])  # Saída: 1
print(tupla[-1])  # Saída: 5

    # Fatiamento de tupla:
print(tupla[1:4])  # Saída: (2, 3, 4)

    # Concatenação de tuplas:
outra_tupla = (6, 7, 8)
nova_tupla = tupla + outra_tupla
print(nova_tupla)  # Saída: (1, 2, 3, 4, 5, 6, 7, 8)

    # Verificando se um elemento está presente na tupla:
if 3 in tupla:
    print("O elemento 3 está presente na tupla.")
else:
    print("O elemento 3 não está presente na tupla.")

    # Contando ocorrências de um elemento na tupla:
contagem = tupla.count(3)
print("O número 3 aparece", contagem, "vezes na tupla.")

    # Encontrando o índice de um elemento na tupla:
indice = tupla.index(4)
print("O índice do número 4 na tupla é:", indice)

    # Desempacotamento de tupla:
a, b, c = (1, 2, 3)
print("a:", a)  # Saída: 1
print("b:", b)  # Saída: 2
print("c:", c)  # Saída: 3

    # Iterando sobre os elementos de uma tupla:
for elemento in tupla:
    print(elemento)

    # Tamanho de uma tupla:
print(len(tupla))  # Saída: 5

    # Criando uma tupla vazia:
tupla_vazia = ()

    # Atribuindo uma única variável a uma tupla (tupla de um único elemento):
tupla_unica = (1,)
