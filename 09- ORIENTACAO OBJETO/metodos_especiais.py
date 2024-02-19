'''
    Métodos Especiais:
        Métodos especiais são métodos que têm um significado especial em Python e são chamados automaticamente em determinadas situações.
        Eles são definidos com dois underscores (__) no início e no final do nome do método.

    Alguns exemplos de métodos especiais:
   
    __init__: é um método especial usado para inicializar os atributos de um objeto quando ele é criado.
    __str__: Retorna uma representação em string do objeto quando chamado pela função str().
    __repr__: Retorna uma representação em string do objeto que pode ser usada para recriar o objeto quando chamado pela função repr().
    __len__: Retorna o comprimento do objeto quando chamado pela função len().
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"
