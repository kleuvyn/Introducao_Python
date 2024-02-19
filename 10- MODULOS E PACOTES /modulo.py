'''
    Módulo:
        Um módulo é um arquivo contendo definições e instruções Python.
        O nome do arquivo é o nome do módulo com a extensão .py.
        Os módulos podem conter variáveis, funções e classes.
        Você pode importar um módulo em outro arquivo Python para reutilizar seu código.
'''
# meu_modulo.py
def saudacao(nome):
    return f"Olá, {nome}!"

def soma(a, b):
    return a + b

PI = 3.14159

#Para utilizar esse módulo em outro arquivo Python, você pode importá-lo da seguinte forma:

# TODO import meu_modulo

# print(meu_modulo.saudacao("João"))  # Saída: Olá, João!
# print(meu_modulo.soma(3, 5))  # Saída: 8
# print(meu_modulo.PI)  # Saída: 3.14159
