'''
Os dicionários são estruturas de dados muito versáteis e poderosas que permitem armazenar dados em pares chave-valor.
Os dicionários são extremamente flexíveis e úteis para armazenar e manipular dados em Python, especialmente quando você precisa associar valores a chaves para uma rápida recuperação posterior.
'''
    # Criação de um dicionário:
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

    # Acessando valores de um dicionário:
print(dicionario['chave1'])  # Saída: valor1

    # Adicionando um novo par chave-valor:
dicionario['nova_chave'] = 'novo_valor'

    # Removendo um par chave-valor:
del dicionario['chave1']

    # Verificando se uma chave está presente no dicionário:
if 'chave1' in dicionario:
    print("A chave1 está presente no dicionário.")

    # Iterando sobre chaves e valores do dicionário:
for chave, valor in dicionario.items():
    print(chave, valor)

    # Obtendo todas as chaves do dicionário:
chaves = dicionario.keys()

    # Obtendo todos os valores do dicionário:
valores = dicionario.values()

    # Verificando o tamanho do dicionário (número de pares chave-valor):
tamanho = len(dicionario)

    # Criando um dicionário vazio:
dicionario_vazio = {}

    # Copiando um dicionário:
copia_dicionario = dicionario.copy()

    # Limpando um dicionário:
dicionario.clear()

    # Combinando dois dicionários:
outro_dicionario = {'outra_chave': 'outro_valor'}
dicionario.update(outro_dicionario)

    # Obtendo um valor com uma chave específica, com um valor padrão se a chave não existir:
valor = dicionario.get('chave_inexistente', 'valor_padrao')

    # Definindo um valor padrão para uma nova chave:
dicionario.setdefault('nova_chave', 'valor_padrao')