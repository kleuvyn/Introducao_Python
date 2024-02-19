'''
Uma função  é um bloco de código reutilizável que executa uma tarefa específica. Ela recebe dados (parâmetros) como entrada, realiza algumas operações com esses dados e pode retornar um resultado. As funções ajudam a organizar o código, tornando-o mais legível e fácil de manter.
'''

def somar(a, b):
    # Bloco de código da função
    # Pode usar os parâmetros e fazer operações
    resultado = a + b
    return resultado

# Chamando a função e atribuindo o resultado a uma variável
resultado_soma = somar(3, 5)
print(resultado_soma)  # Saída: 8
