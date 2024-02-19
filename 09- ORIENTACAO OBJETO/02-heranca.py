'''
    Herança:
        Herança é um mecanismo que permite que uma classe herde atributos e métodos de outra classe.
        A classe que herda é chamada de classe filha ou subclasse, e a classe da qual ela herda é chamada de classe pai ou superclasse.
'''
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
