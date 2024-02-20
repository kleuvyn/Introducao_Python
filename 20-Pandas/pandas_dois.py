import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados de um arquivo CSV
df = pd.read_csv('dados_vendas.csv')

# Exibindo as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# Resumo estatístico dos dados numéricos
print("\nResumo Estatístico:")
print(df.describe())

# Contagem de valores únicos em uma coluna categórica
print("\nContagem de Valores Únicos por Região:")
print(df['Região'].value_counts())

# Filtrando os dados por uma condição
df_filtro = df[df['Valor_Venda'] > 1000]

# Agrupando os dados por região e calculando a média de vendas
df_grouped = df.groupby('Região').mean()['Valor_Venda']

# Visualizando os resultados em um gráfico de barras
df_grouped.plot(kind='bar', color='skyblue')
plt.title('Média de Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Média de Vendas')
plt.xticks(rotation=45)
plt.show()
