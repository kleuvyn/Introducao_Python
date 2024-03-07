# Dia 5: Escreva um programa que solicite ao usuário que insira um número e imprima a tabuada desse número.

print( 'Sua tabuada na mão \n')

print("Selecione um operador: +, -, *, /")
operador = input("Operador: ")

if operador in ['+', '-', '*', '/']:
    print("Operador selecionado:", operador)
else:
    print("Operador inválido. Por favor, selecione +, -, * ou /.")


numero = int(input('Qual é o número: '))

if operador == '+':
    for i in range(11):
        adicao = numero + i
        print(f'{numero} + {i} = {adicao}')


elif operador == '-':
    for i in range(11):
        subtracao = numero  - i
        print(f'{numero} - {i} = {subtracao}')

elif operador == '*':
    for i in range(11):
        multiplicacao = numero  * i
        print(f'{numero} * {i} = {multiplicacao}')

elif operador == '/':
    for i in range(1, 11):  
        divisao = numero / i
        print(f'{numero} / {i} = {divisao:.2f}')
        
else:
    print('!!! ERRO !!! \n Número Invalido')
