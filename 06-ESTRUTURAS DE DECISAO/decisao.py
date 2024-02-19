'''
Em Python, não há uma estrutura de switch-case como em algumas outras linguagens de programação. No entanto, você pode obter um comportamento semelhante usando um dicionário e funções.

No entanto, se você deseja uma solução que se assemelhe mais a um switch-case, pode usar uma biblioteca externa como *pySwitch*.

pySwitch é uma biblioteca Python que permite emular a funcionalidade de switch-case. Você pode instalar essa biblioteca usando o pip:
'''
#pip install pyswitch

# TODO Aqui está um exemplo de como você pode usar pySwitch:


from construct import Switch


def opcao1():
    print("Você escolheu a opção 1")

def opcao2():
    print("Você escolheu a opção 2")

def opcao3():
    print("Você escolheu a opção 3")

def opcao_padrao():
    print("Opção inválida")

opcao = 2

with Switch(opcao) as s: # as (como)
    s.case(1, opcao1)
    s.case(2, opcao2)
    s.case(3, opcao3)
    s.default(opcao_padrao)

'''
Segunda opção, você pode usar uma combinação de if, elif e else para alcançar o mesmo efeito.

# TODO Aqui está uma abordagem alternativa para implementar um comportamento semelhante ao switch-case em Python usando dicionários e funções:
'''
def opcao1():
    print("Você escolheu a opção 1")

def opcao2():
    print("Você escolheu a opção 2")

def opcao3():
    print("Você escolheu a opção 3")

def opcao_padrao():
    print("Opção inválida")

opcoes = {
    1: opcao1,
    2: opcao2,
    3: opcao3,
}

def escolher_opcao(opcao):
    func = opcoes.get(opcao, opcao_padrao)
    func()

# Exemplo de uso
escolher_opcao(2)  # Saída: Você escolheu a opção 2
escolher_opcao(5)  # Saída: Opção inválida

'''
Neste exemplo:

Definimos funções para cada opção que queremos suportar.
Criamos um dicionário onde as chaves são os valores possíveis que a variável de escolha pode ter e os valores são as funções correspondentes.
Definimos uma função escolher_opcao(opcao) que usa opcoes.get(opcao, opcao_padrao) para obter a função correspondente com base no valor da opção escolhida. Se o valor da opção não estiver no dicionário, ele usa a função opcao_padrao.
Chamamos escolher_opcao() com o valor da opção para executar a função correspondente.

Essa abordagem pode ser útil quando você precisa de funcionalidade semelhante ao switch-case em Python.
#TODO No entanto, é importante notar que o uso excessivo dessa técnica pode levar a um código menos legível e mais complicado. Em muitos casos, uma estrutura de if-elif-else simples pode ser mais apropriada e clara.
'''