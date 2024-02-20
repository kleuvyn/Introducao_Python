'''
Expressões regulares, também conhecidas como regex, são padrões de busca utilizados para encontrar padrões específicos em strings. Elas fornecem uma maneira flexível e poderosa de pesquisar e manipular texto em Python e em muitas outras linguagens de programação.

Em Python, o módulo re fornece suporte para expressões regulares. 
'''
import re

# Procura por ocorrências de "python" ou "Python" em uma string
texto = "Python é uma linguagem de programação poderosa."
padrao = r"python"
resultado = re.search(padrao, texto, re.IGNORECASE)
if resultado:
    print("Padrão encontrado:", resultado.group())
else:
    print("Padrão não encontrado.")

# Substitui todas as ocorrências de "python" por "Java" em uma string
novo_texto = re.sub(r"python", "Java", texto, flags=re.IGNORECASE)
print("Texto modificado:", novo_texto)


# Exemplo de texto
texto = """
Exemplo de texto com várias linhas.
Este texto contém números como 12345 e também palavras como Python e programação.
Vamos ver como podemos usar expressões regulares para manipular este texto.
"""

'''Busca por padrões:
        re.search(pattern, string): Procura por um padrão em toda a string e retorna um objeto de correspondência se encontrar ou None caso contrário.
        re.match(pattern, string): Procura por um padrão apenas no início da string e retorna um objeto de correspondência se encontrar ou None caso contrário.'''
# Busca por padrões
padrao_busca = r"\b\w{6}\b"  # Padrão: palavras de exatamente 6 caracteres
resultados_busca = re.findall(padrao_busca, texto)
print("Palavras de 6 caracteres encontradas:", resultados_busca)


''' Correspondência de padrões:
        re.findall(pattern, string): Encontra todas as ocorrências do padrão na string e retorna uma lista com as correspondências.
        re.finditer(pattern, string): Encontra todas as ocorrências do padrão na string e retorna um iterador com objetos de correspondência.'''
# Correspondência de padrões
padrao_correspondencia = r"\bPython\b"  # Padrão: a palavra "Python"
correspondencia = re.search(padrao_correspondencia, texto)
if correspondencia:
    print("Correspondência encontrada:", correspondencia.group())
else:
    print("Nenhuma correspondência encontrada.")


    '''Substituição de padrões:
        re.sub(pattern, replacement, string): Substitui todas as ocorrências do padrão na string pelo texto de substituição especificado.
        re.subn(pattern, replacement, string): Semelhante ao re.sub(), mas retorna uma tupla com o texto resultante e o número de substituições feitas.'''
    # Substituição de padrões
novo_texto = re.sub(r"\bPython\b", "Java", texto)  # Substitui "Python" por "Java"
print("Texto modificado:", novo_texto)

'''Modificadores:
        re.IGNORECASE ou re.I: Ignora a distinção entre maiúsculas e minúsculas durante a correspondência.
        re.MULTILINE ou re.M: Permite correspondências multilineares, alterando o comportamento dos metacaracteres ^ e $.'''
# Modificadores
padrao_modificador = r"^Este"  # Padrão: a palavra "Este" no início da linha
correspondencia_modificador = re.search(padrao_modificador, texto, re.MULTILINE)
if correspondencia_modificador:
    print("Correspondência com modificador encontrada:", correspondencia_modificador.group())
else:
    print("Nenhuma correspondência com modificador encontrada.")

'''Padrões especiais:
        .: Corresponde a qualquer caractere, exceto uma nova linha.
        ^: Corresponde ao início da string.
        $: Corresponde ao final da string.
        \b: Corresponde a uma borda de palavra.
        \d, \w, \s: Corresponde a um dígito, um caractere de palavra ou um espaço em branco, respectivamente.
        []: Corresponde a qualquer caractere dentro dos colchetes.
        [^]: Corresponde a qualquer caractere que não esteja dentro dos colchetes.
'''
import re

# Exemplo de texto
texto = "Olá mundo 123."

# Padrão especial '.': Corresponde a qualquer caractere, exceto uma nova linha.
padrao_ponto = r"."
resultado_ponto = re.findall(padrao_ponto, texto)
print("Correspondências para '.':", resultado_ponto)

# Padrão especial '^': Corresponde ao início da string.
padrao_inicio = r"^Olá"
resultado_inicio = re.match(padrao_inicio, texto)
if resultado_inicio:
    print("Correspondência para '^':", resultado_inicio.group())
else:
    print("Nenhuma correspondência para '^'.")

# Padrão especial '$': Corresponde ao final da string.
padrao_final = r"123.$"
resultado_final = re.search(padrao_final, texto)
if resultado_final:
    print("Correspondência para '$':", resultado_final.group())
else:
    print("Nenhuma correspondência para '$'.")

# Padrão especial '\b': Corresponde a uma borda de palavra.
padrao_borda = r"\bmundo\b"
resultado_borda = re.search(padrao_borda, texto)
if resultado_borda:
    print("Correspondência para '\\b':", resultado_borda.group())
else:
    print("Nenhuma correspondência para '\\b'.")

# Padrão especial '\d': Corresponde a um dígito.
padrao_digito = r"\d"
resultado_digito = re.findall(padrao_digito, texto)
print("Correspondências para '\\d':", resultado_digito)

# Padrão especial '\w': Corresponde a um caractere de palavra.
padrao_palavra = r"\w+"
resultado_palavra = re.findall(padrao_palavra, texto)
print("Correspondências para '\\w+':", resultado_palavra)

# Padrão especial '\s': Corresponde a um espaço em branco.
padrao_espaco = r"\s"
resultado_espaco = re.findall(padrao_espaco, texto)
print("Correspondências para '\\s':", resultado_espaco)

# Padrão especial '[]': Corresponde a qualquer caractere dentro dos colchetes.
padrao_colchetes = r"[aeiou]"
resultado_colchetes = re.findall(padrao_colchetes, texto)
print("Correspondências para '[aeiou]':", resultado_colchetes)

# Padrão especial '[^]': Corresponde a qualquer caractere que não esteja dentro dos colchetes.
padrao_negacao_colchetes = r"[^aeiou]"
resultado_negacao_colchetes = re.findall(padrao_negacao_colchetes, texto)
print("Correspondências para '[^aeiou]':", resultado_negacao_colchetes)


'''Quantificadores:
        *: Corresponde a zero ou mais ocorrências do padrão anterior.
        +: Corresponde a uma ou mais ocorrências do padrão anterior.
        ?: Corresponde a zero ou uma ocorrência do padrão anterior.
        {m}: Corresponde exatamente a m ocorrências do padrão anterior.
        {m, n}: Corresponde a pelo menos m e no máximo n ocorrências do padrão anterior.
'''
import re

# Exemplo de texto
texto = "aabbcc"

# Padrão com o quantificador '*': Corresponde a zero ou mais ocorrências do padrão anterior.
padrao_asterisco = r"ab*"
resultado_asterisco = re.findall(padrao_asterisco, texto)
print("Correspondências para 'ab*':", resultado_asterisco)

# Padrão com o quantificador '+': Corresponde a uma ou mais ocorrências do padrão anterior.
padrao_mais = r"ab+"
resultado_mais = re.findall(padrao_mais, texto)
print("Correspondências para 'ab+':", resultado_mais)

# Padrão com o quantificador '?': Corresponde a zero ou uma ocorrência do padrão anterior.
padrao_interrogacao = r"ab?"
resultado_interrogacao = re.findall(padrao_interrogacao, texto)
print("Correspondências para 'ab?':", resultado_interrogacao)

# Padrão com o quantificador '{m}': Corresponde exatamente a 'm' ocorrências do padrão anterior.
padrao_exato = r"ab{2}"
resultado_exato = re.findall(padrao_exato, texto)
print("Correspondências para 'ab{2}':", resultado_exato)

# Padrão com o quantificador '{m, n}': Corresponde a pelo menos 'm' e no máximo 'n' ocorrências do padrão anterior.
padrao_intervalo = r"ab{1,2}"
resultado_intervalo = re.findall(padrao_intervalo, texto)
print("Correspondências para 'ab{1,2}':", resultado_intervalo)
