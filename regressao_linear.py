import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# Importação das bibliotecas necessárias e módulos

# GERANDO UMA AMOSTRA RANDOMICA
# Geração de uma amostra de dados aleatórios para x e y com ruído
x, y = make_regression(n_samples=200, n_features=1, noise=30)

# Plotagem da amostra gerada
plt.scatter(x, y)

# CRIANDO UM MODELO DE REGRESSÃO LINEAR
# Instanciação do modelo de regressão linear
modelo = LinearRegression()

# Ajuste do modelo aos dados
modelo.fit(x, y)

# Extração dos coeficientes angular e linear do modelo ajustado
coeficiente_angular = modelo.coef_
coeficiente_linear = modelo.intercept_

# FUNÇÃO PARA PREVER O VALOR DE Y  (y = a + b * x)
# Previsão dos valores de y utilizando os coeficientes encontrados
y_pred = coeficiente_linear + coeficiente_angular * x

# Impressão dos coeficientes encontrados
print('Coeficiente Angular: {0}\nCoeficiente Linear: {1}'.format(coeficiente_angular, coeficiente_linear))

# Plotagem dos dados e da linha de regressão ajustada
plt.scatter(x, y)
plt.plot(x, coeficiente_linear + coeficiente_angular * x, color='red') # Linha de regressão
plt.scatter(2.5, coeficiente_linear + coeficiente_angular * 2.5, color='green') # Ponto de exemplo
plt.show()
