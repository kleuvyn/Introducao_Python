'''
Os operadores são símbolos especiais que realizam operações em operandos (valores ou variáveis).

    Operadores Aritméticos:
        Usados para realizar operações matemáticas básicas.
'''
soma = 5 + 3   # Adição
subtracao = 7 - 2   # Subtração
multiplicacao = 4 * 6   # Multiplicação
divisao = 10 / 2   # Divisão
resto_divisao = 10 % 3   # Resto da divisão
exponenciacao = 2 ** 3   # Exponenciação

'''
    Operadores de Comparação:
        Usados para comparar valores e retornar um resultado booleano.
'''
igualdade = 5 == 5   # Igual a
diferenca = 6 != 3   # Diferente de
maior_que = 8 > 3   # Maior que
menor_que = 4 < 7   # Menor que
maior_ou_igual = 9 >= 9   # Maior ou igual a
menor_ou_igual = 5 <= 5   # Menor ou igual a

'''
    Operadores Lógicos:
        Usados para combinar expressões lógicas e retornar um resultado booleano.

    AND (e):
        Retorna True se ambas as expressões forem verdadeiras.
'''
a = True
b = False
resultado = a and b
print(resultado)  # Saída: False

'''
    OR (ou):
        Retorna True se pelo menos uma das expressões for verdadeira.
'''
a = True
b = False
resultado = a or b
print(resultado)  # Saída: True

'''
    NOT (não):
        Inverte o valor da expressão, retornando True se a expressão for falsa e False se a expressão for verdadeira.
'''
a = True
resultado = not a
print(resultado)  # Saída: False

'''
    Operadores de Atribuição:
        Usados para atribuir valores a variáveis.
'''
x = 5   # Atribuição simples
x += 2   # Adição e atribuição (equivalente a x = x + 2)
x -= 3   # Subtração e atribuição (equivalente a x = x - 3)
x *= 4   # Multiplicação e atribuição (equivalente a x = x * 4)
x /= 2   # Divisão e atribuição (equivalente a x = x / 2)

'''
    Operadores de Identidade:
        Usados para verificar se dois objetos têm a mesma identidade. is (é)
'''
x = [1, 2, 3]
y = [1, 2, 3]
identidade = x is y   # Retorna False porque x e y são objetos diferentes

'''
    Operadores de Associação:
        Usados para verificar se um valor está presente em uma sequência. in(em)
'''
lista = [1, 2, 3, 4, 5]
associacao = 3 in lista   # Retorna True porque 3 está na lista
