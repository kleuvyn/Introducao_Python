'''
    Encapsulamento:
        Encapsulamento é o conceito de restringir o acesso direto aos atributos e métodos de uma classe.
        Em Python, isso é frequentemente alcançado usando métodos getters e setters para acessar e modificar os atributos.
'''
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):  # Método getter
        return self.__saldo

