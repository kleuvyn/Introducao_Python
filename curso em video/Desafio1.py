# Desafio 1
#Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

nome = str(input('Qual é o seu nome? '))
boas_vindas = f'Olá {nome}! Seja muito bem-vinda! Este é um espaço para compartilhar conhecimentos, aprender juntos e aproveitar a jornada. Sinta-se à vontade para participar das conversas, fazer perguntas e contribuir com suas experiências. Estamos aqui para nos apoiar mutuamente. Seja bem-vinda à nossa comunidade! 🚀✨'

print(boas_vindas)

# Desafio 2
# Crie um script que leia o dia, mês e o ano da data de nascimento e mostre uma mensagem formatada

dia = int(input('Qual dia você nasceu: '))
mes = int(input('Qual mês você nasceu: '))
ano = int(input('Qual ano você nasceu: '))
nascimento = f'Olá {nome}, você nasceu em {dia}/{mes}/{ano}.'

print(nascimento)#

# Desafio 3
# Crie um script que leia dois números e mostre a soma entre eles
print('Vamos somar!!!')
primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
soma_numeros = primeiro_numero + segundo_numero
mensagem_soma = f'A soma de {primeiro_numero} + {segundo_numero} é igual a {soma_numeros}.'

print(mensagem_soma)