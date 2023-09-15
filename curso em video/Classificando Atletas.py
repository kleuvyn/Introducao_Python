from datetime import date

print('\nSeja Bem-Vindo(a) à Confederação Nacional de Natação1\n')

atual = date.today().year
nome = str(input('Digite seu nome:\n')).capitalize()
sobrenome = str(input('Digite seu sobrenome:\n'))
ano_de_nascimento = int(input('Digite seu ano de nascimento:\n'))
idade = atual - ano_de_nascimento

if idade <= 9:
    print(nome,'sua categoria, de acordo com a idade é MIRIM')

elif idade <= 14:
    print(nome,'sua categoria, de acordo com a idade é INFANTIL')

elif idade <= 19:
    print(nome,'sua categoria, de acordo com a idade é JÚNIOR')

elif idade <= 25:
    print(nome, 'sua categoria, de acordo com a idade é SÊNIOR')

else:
    print(nome,'sua categoria, de acordo com a idade é MASTER')
