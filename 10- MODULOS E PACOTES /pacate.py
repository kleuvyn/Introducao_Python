'''
    Pacote:
        Um pacote é uma coleção de módulos organizados em diretórios.
        Cada diretório dentro do pacote pode conter módulos ou subpacotes.
        Um pacote é identificado por um arquivo especial chamado __init__.py, que pode estar vazio ou conter inicializações de código.
        Os pacotes permitem organizar e estruturar grandes projetos Python em unidades mais gerenciáveis e reutilizáveis.

meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
    subpacote/
        __init__.py
        modulo3.py

Para importar um módulo de dentro de um pacote, você pode fazer o seguinte:

# TODO from meu_pacote import modulo1

print(modulo1.funcao1())

Para importar um módulo de dentro de um subpacote:

# TODO from meu_pacote.subpacote import modulo3

print(modulo3.funcao3())

'''