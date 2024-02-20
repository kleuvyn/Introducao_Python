# Gráfico de Linhas:
import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criando o gráfico de linhas
plt.plot(x, y)

# Adicionando título e rótulos dos eixos
plt.title('Gráfico de Linhas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.show()

# Gráfico de Barras:
import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Criando o gráfico de barras
plt.bar(categorias, valores)

# Adicionando título e rótulos dos eixos
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibindo o gráfico
plt.show()

# Gráfico de Dispersão:
import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criando o gráfico de dispersão
plt.scatter(x, y)

# Adicionando título e rótulos dos eixos
plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.show()

# Histograma:
import matplotlib.pyplot as plt
import numpy as np

# Dados
dados = np.random.randn(1000)

# Criando o histograma
plt.hist(dados, bins=30, color='skyblue', edgecolor='black')

# Adicionando título e rótulos dos eixos
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')

# Exibindo o gráfico
plt.show()
