'''
    Getter (Método de Acesso):
        Um getter é um método que permite acessar o valor de um atributo privado de uma classe.
        Ele fornece uma maneira de ler o valor de um atributo sem acessá-lo diretamente.
        Geralmente, os getters têm o prefixo get, seguido pelo nome do atributo que estão recuperando.
'''
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado

    def get_nome(self):  # Getter para acessar o atributo privado
        return self.__nome

pessoa = Pessoa("João")
print(pessoa.get_nome())  # Saída: João


'''
    Setter (Método de Modificação):
        Um setter é um método que permite modificar o valor de um atributo privado de uma classe.
        Ele fornece uma maneira de definir o valor de um atributo sem modificá-lo diretamente.
        Geralmente, os setters têm o prefixo set, seguido pelo nome do atributo que estão modificando.
'''
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado

    def set_nome(self, novo_nome):  # Setter para modificar o atributo privado
        self.__nome = novo_nome

pessoa = Pessoa("João")
print(pessoa.get_nome())  # Saída: João
pessoa.set_nome("Maria")
print(pessoa.get_nome())  # Saída: Maria
