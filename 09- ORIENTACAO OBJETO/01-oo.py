'''
Orientação a objetos é um paradigma de programação que organiza o código em torno de objetos, que podem conter dados na forma de campos (também conhecidos como atributos ou propriedades) e código na forma de procedimentos (métodos ou funções). Em Python, como em muitas outras linguagens, a orientação a objetos é uma parte fundamental da linguagem.
'''

'''
    Classe:
        Uma classe é um modelo ou plano para criar objetos. Define os atributos e métodos que os objetos terão.
        Em Python, as classes são definidas usando a palavra-chave class.
'''
class Pessoa:
    def __init__(self, nome, idade): # self (auto) 
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

'''
    Objeto:
        Um objeto é uma instância de uma classe. É uma entidade que possui atributos e métodos específicos definidos pela classe.
        Para criar um objeto, você instancia a classe.
'''
pessoa1 = Pessoa("Ana", 30)
pessoa2 = Pessoa("João", 25)

'''
    Atributos:
        Atributos são variáveis associadas a um objeto. Eles armazenam dados que descrevem o objeto.
        Os atributos em Python são acessados usando a notação de ponto (objeto.atributo).
'''
print(pessoa1.nome)  # Saída: Ana
print(pessoa2.idade)  # Saída: 25

'''
    Métodos:
        Métodos são funções associadas a uma classe. Eles representam o comportamento dos objetos daquela classe.
        Os métodos em Python são definidos dentro da classe e podem ser acessados usando a notação de ponto (objeto.metodo()).
'''
pessoa1.apresentar()  # Saída: Olá, meu nome é Ana e tenho 30 anos.
pessoa2.apresentar()  # Saída: Olá, meu nome é João e tenho 25 anos.

'''
    Construtor (__init__):
        O método __init__ é um método especial usado para inicializar os atributos de um objeto quando ele é criado.
'''