'''A classificação é uma das tarefas mais comuns em machine learning, e o scikit-learn (SKLearn) é uma biblioteca popular e para construir modelos de classificação. Aqui está um exemplo básico de como realizar classificação com o SKLearn:
'''
# Importando as bibliotecas necessárias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carregando o conjunto de dados de exemplo (Iris dataset)
iris = load_iris()

# Dividindo o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Criando e treinando um classificador de SVM (Support Vector Machine)
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
y_pred = clf.predict(X_test)

# Avaliando a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisão do modelo:", accuracy)
