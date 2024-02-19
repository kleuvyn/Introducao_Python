'''
Em Python, a manipulação de arquivos é feita usando funções e métodos fornecidos pelo módulo embutido `open()`. Este módulo permite que você abra, leia, escreva e manipule arquivos de texto e binários.


1. **Abrindo um arquivo para leitura:**

# Abre o arquivo no modo de leitura ('r')

with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

2. **Abrindo um arquivo para escrita:**

# Abre o arquivo no modo de escrita ('w')

with open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um arquivo de texto.\n')

3. **Modos de abertura de arquivo:**

   - `'r'`: Abre o arquivo para leitura (padrão).
   - `'w'`: Abre o arquivo para escrita. Se o arquivo já existir, ele será sobrescrito. Se não existir, um novo arquivo será criado.
   - `'a'`: Abre o arquivo para adição, ou seja, os novos dados serão adicionados ao final do arquivo.
   - `'b'`: Modo binário. Adicione isso a qualquer um dos modos acima para abrir um arquivo em modo binário. Ex: `'rb'` ou `'wb'`.
   - `'+'`: Modo de atualização (leitura e escrita). Adicione isso a qualquer um dos modos acima para abrir um arquivo tanto para leitura quanto para escrita. Ex: `'r+'`, `'w+'`, `'a+'`.

4. **Leitura de um arquivo linha por linha:**

with open('arquivo.txt', 'r') as arquivo:

    for linha in arquivo:
        print(linha.strip())  # strip() remove espaços em branco e quebras de linha desnecessárias

5. **Escrita de uma lista de strings em um arquivo:**

linhas = ['Linha 1\n', 'Linha 2\n', 'Linha 3\n']

with open('arquivo.txt', 'w') as arquivo:
    arquivo.writelines(linhas)

6. **Outras operações de arquivo:**
   - `read(size)`: Lê `size` bytes do arquivo.
   - `readline()`: Lê uma linha do arquivo.
   - `readlines()`: Lê todas as linhas do arquivo em uma lista.
   - `seek(offset)`: Move o ponteiro de arquivo para a posição `offset` no arquivo.
   - `tell()`: Retorna a posição atual do ponteiro de arquivo.

OBS: 
Certifique-se de sempre usar a instrução `with` ao manipular arquivos em Python, pois ela garante que o arquivo seja fechado corretamente após a conclusão das operações de leitura ou escrita. Isso ajuda a prevenir vazamentos de recursos e erros de manipulação de arquivo.
'''