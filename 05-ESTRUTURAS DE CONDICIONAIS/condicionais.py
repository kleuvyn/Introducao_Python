'''
A estrutura condicional é usada para executar diferentes blocos de código com base em condições específicas. As estruturas condicionais mais comuns são as instruções if, elif (abreviação de "else if") e else. 

Instrução if:

        Utilizada para executar um bloco de código se uma condição for verdadeira
'''
# TODO if condicao:
    # Bloco de código a ser executado se a condição for verdadeira

idade = 18
if idade >= 18:
    print("Você é maior de idade.")


'''    
Instrução elif:
        Utilizada para verificar condições adicionais se a primeira condição (if) for falsa.
        Pode haver vários elif em uma estrutura condicional.
'''
# TODO if condicao1:
    # Bloco de código a ser executado se a condicao1 for verdadeira
# TODO elif condicao2:
    # Bloco de código a ser executado se a condicao2 for verdadeira
nota = 75
if nota >= 90:
    print("Nota A")
elif nota >= 80:
    print("Nota B")
elif nota >= 70:
    print("Nota C")


'''    
Instrução else:
        Utilizada para executar um bloco de código se nenhuma das condições anteriores for verdadeira.
'''
# TODO if condicao:
    # Bloco de código a ser executado se a condicao for verdadeira
# TODO else:
    # Bloco de código a ser executado se a condicao for falsa
idade = 15
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
