'''
Tratamento de exceções em Python permite lidar com erros e exceções que podem ocorrer durante a execução do programa, permitindo que o código continue a ser executado de forma controlada. Isso é particularmente útil para lidar com situações inesperadas que podem surgir durante a execução do programa.

Em Python, o tratamento de exceções é feito usando blocos try, except e, opcionalmente, finally:

'''
# Bloco try:
#         Este bloco contém o código que pode gerar uma exceção.
try:
    # Código que pode gerar uma exceção
    x = 10 / 0

# Bloco except:
#         Este bloco é executado quando uma exceção é levantada dentro do bloco try.
#         Você pode especificar o tipo de exceção que deseja capturar ou usar um bloco except genérico para capturar qualquer exceção.
    
except ZeroDivisionError:
    # Tratamento específico para a exceção ZeroDivisionError
    print("Erro: Divisão por zero.")

except Exception as e:
    # Tratamento genérico para outras exceções
    print(f"Erro inesperado: {e}")

#Bloco finally (opcional):
#         Este bloco é executado sempre, independentemente de uma exceção ser levantada ou não.
#         É usado para realizar ações de limpeza, como fechar arquivos ou liberar recursos.

finally:
    # Bloco opcional de limpeza
    print("Executando o bloco finally.")

'''
Além disso, você também pode usar a cláusula else após todos os blocos except. O código dentro do bloco else é executado se nenhum erro ocorrer durante a execução do bloco try.
'''
try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
else:
    print(f"Você digitou o número {x}.")
