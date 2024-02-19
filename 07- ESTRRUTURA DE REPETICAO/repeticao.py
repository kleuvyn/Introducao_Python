'''
Em Python, existem duas estruturas de repetição principais: for e while. Essas estruturas são usadas para executar um bloco de código repetidamente, com base em uma condição específica. Aqui está uma visão geral de cada uma delas:
'''
'''
#TODO Loop for:
        O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, string, etc.) ou um iterável.
        Ele executa um bloco de código uma vez para cada item na sequência ou iterável.
'''
sequencia = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for item in sequencia:
    # Bloco de código a ser repetido para cada item na sequência
    print(sequencia)

nomes = ["Ana", "João", "Maria"]

for nome in nomes:
    print(nome)


'''
#TODO Loop while:
        O loop while executa um bloco de código repetidamente enquanto uma condição específica for verdadeira.
        É importante garantir que a condição em um loop while eventualmente se torne falsa; caso contrário, o loop pode se tornar infinito.
'''
contador = 0
while contador < 5:
      # Bloco de código a ser repetido enquanto a condição for verdadeira

    print(contador)
    contador += 1

'''
Dentro de cada loop, você pode usar as instruções break e continue para controlar o fluxo de execução do loop:

    #TODO break: Encerra imediatamente o loop.
    continue: Pula para a próxima iteração do loop, ignorando o código restante dentro do bloco do loop atual.

Exemplo de uso de break:
'''