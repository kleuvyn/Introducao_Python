## 1: Criando e Manipulando um DataFrame

import pandas as pd

# Criando um DataFrame a partir de um dicionário
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'Idade': [25, 30, 35, 40],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']}
df = pd.DataFrame(data)

# Imprimindo o DataFrame
print("DataFrame original:")
print(df)

# Adicionando uma nova coluna
df['Sexo'] = ['F', 'M', 'M', 'M']

# Removendo uma coluna
df.drop(columns=['Cidade'], inplace=True)

# Imprimindo o DataFrame atualizado
print("\nDataFrame atualizado:")
print(df)

## 2: Leitura e Escrita de Dados

# Leitura de dados de um arquivo CSV
df_csv = pd.read_csv('dados.csv')

# Escrita de dados para um arquivo Excel
# df_excel.to_excel('dados.xlsx', index=False)

## 3: Análise de Dados e Estatísticas Descritivas

# Resumo estatístico dos dados
summary_stats = df.describe()

# Contagem de valores únicos em uma coluna
value_counts = df['Sexo'].value_counts()

# Média de idade
mean_age = df['Idade'].mean()

# Mediana de idade
median_age = df['Idade'].median()

# Imprimindo os resultados
print("Resumo Estatístico:")
print(summary_stats)
print("\nContagem de Valores Únicos:")
print(value_counts)
print("\nMédia de Idade:", mean_age)
print("Mediana de Idade:", median_age)

## 4: Visualização de Dados (com Matplotlib)

import matplotlib.pyplot as plt

# Gráfico de barras da contagem de valores únicos
value_counts.plot(kind='bar', color='skyblue')
plt.title('Contagem de Valores Únicos por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()
