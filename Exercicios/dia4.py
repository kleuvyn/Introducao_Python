# Dia 4: Escreva um programa que converta graus Celsius para Fahrenheit. O usuário deve fornecer a temperatura em Celsius.

print('Conversor de  graus Celsius para Fahrenheit \n')

celsius = float(input(' Qual é a temperatura hoje na sua região: \n '))

fahrenheit = 9/5 * celsius + 32 

print(f' A temperatura hoje está {fahrenheit}graus \n')

# ---------------------------------------------

print('Conversor de  graus Fahrenheit para Celsius \n')

fahrenheit  = float(input(' Qual é a temperatura hoje na sua região: '))

celsius = 5/9 * (fahrenheit - 32)

print(f' A temperatura hoje está {celsius}graus ')