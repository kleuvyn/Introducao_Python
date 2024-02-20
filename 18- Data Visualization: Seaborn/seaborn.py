'''Seaborn é uma biblioteca Python baseada em matplotlib que fornece uma interface de alto nível para criação de visualizações estatísticas atraentes e informativas. Ele é particularmente útil para criar gráficos estatísticos complexos com facilidade. Aqui estão alguns exemplos de como explorar dados usando Seaborn:'''

'''Gráficos de dispersão (Scatter plots):
        Úteis para visualizar a relação entre duas variáveis numéricas.'''

import seaborn as sns
import matplotlib.pyplot as plt

# Carregando dados de exemplo
iris = sns.load_dataset("iris")

# Gráfico de dispersão entre comprimento e largura da pétala
sns.scatterplot(x="petal_length", y="petal_width", data=iris)
plt.title("Relação entre comprimento e largura da pétala")
plt.show()

'''Gráficos de linha (Line plots):
        Adequados para visualizar tendências ao longo do tempo ou em séries temporais.'''

import seaborn as sns
import matplotlib.pyplot as plt

# Carregando dados de exemplo
fmri = sns.load_dataset("fmri")

# Gráfico de linha para a atividade cerebral ao longo do tempo
sns.lineplot(x="timepoint", y="signal", data=fmri)
plt.title("Atividade cerebral ao longo do tempo")
plt.show()

'''Histogramas:
        Úteis para visualizar a distribuição de uma variável numérica.'''

import seaborn as sns
import matplotlib.pyplot as plt

# Carregando dados de exemplo
tips = sns.load_dataset("tips")

# Histograma da distribuição das gorjetas
sns.histplot(data=tips, x="tip")
plt.title("Distribuição das gorjetas")
plt.show()

'''Gráficos de barras (Bar plots):
    Úteis para comparar a distribuição de uma variável categórica.'''

import seaborn as sns
import matplotlib.pyplot as plt

# Carregando dados de exemplo
titanic = sns.load_dataset("titanic")

# Gráfico de barras para a contagem de sobreviventes por classe
sns.countplot(data=titanic, x="class", hue="survived")
plt.title("Contagem de sobreviventes por classe")
plt.show()

'''Heatmaps:
    Úteis para visualizar a relação entre duas variáveis categóricas.'''

import seaborn as sns
import matplotlib.pyplot as plt

# Carregando dados de exemplo
flights = sns.load_dataset("flights")

# Pivotando os dados para criar uma matriz
flights_pivot = flights.pivot("month", "year", "passengers")

# Heatmap mostrando o número de passageiros por mês e ano
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Número de passageiros por mês e ano")
plt.show()
