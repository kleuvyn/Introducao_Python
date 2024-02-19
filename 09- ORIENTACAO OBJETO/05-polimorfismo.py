'''
    Polimorfismo:
        Polimorfismo é a capacidade de diferentes classes compartilharem o mesmo nome de método, mas com comportamentos diferentes.
        Isso permite que um método seja chamado de maneira uniforme em diferentes objetos, independentemente de sua classe.
'''
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

def fazer_barulho(animal):
    print(animal.fazer_som())

cachorro = Cachorro()
gato = Gato()

fazer_barulho(cachorro)  # Saída: Au au!
fazer_barulho(gato)  # Saída: Miau!
