import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

# Quarteto de Anscombe
QA_x1 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
QA_y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

QA_x2 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
QA_y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

QA_x3 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
QA_y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

QA_x4 = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0]
QA_y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]


QA_x1 = np.array(QA_x1)
QA_y1 = np.array(QA_y1)
QA_x2 = np.array(QA_x2)
QA_y2 = np.array(QA_y2)
QA_x3 = np.array(QA_x3)
QA_y3 = np.array(QA_y3)
QA_x4 = np.array(QA_x4)
QA_y4 = np.array(QA_y4)

colunas = pd.MultiIndex.from_product((['I', 'II', 'III', 'IV'], ['x', 'y']), names=['Quarteto', 'Coordenada'])
index = [str(i) for i in range(1,12)]
index = pd.Index(index, name="Obs. ")
QA = pd.DataFrame(np.array([QA_x1, QA_y1, QA_x2, QA_y2, QA_x3, QA_y3, QA_x4, QA_y4]).T, 
                  columns=colunas, index=index)


QA.loc["Mean", :] = QA.mean() 
QA.loc["Std", :] = QA.std()
QA.loc["Var", :] = QA.var()

QA.loc["Corr", ('I', 'x')] = np.corrcoef(QA.loc['1':'11', ('I', 'x')], QA.loc['1':'11', ('I', 'y')])[0,1]
QA.loc["Corr", ('II', 'x')] = np.corrcoef(QA.loc['1':'11', ('II', 'x')], QA.loc['1':'11', ('II', 'y')])[0,1]
QA.loc["Corr", ('III', 'x')] = np.corrcoef(QA.loc['1':'11', ('III', 'x')], QA.loc['1':'11', ('III', 'y')])[0,1]
QA.loc["Corr", ('IV', 'x')] = np.corrcoef(QA.loc['1':'11', ('IV', 'x')], QA.loc['1':'11', ('IV', 'y')])[0,1]
QA.loc["Corr", ('I', 'y')] = np.corrcoef(QA.loc['1':'11', ('I', 'y')], QA.loc['1':'11', ('I', 'x')])[0,1]
QA.loc["Corr", ('II', 'y')] = np.corrcoef(QA.loc['1':'11', ('II', 'y')], QA.loc['1':'11', ('II', 'x')])[0,1]
QA.loc["Corr", ('III', 'y')] = np.corrcoef(QA.loc['1':'11', ('III', 'y')], QA.loc['1':'11', ('III', 'x')])[0,1]
QA.loc["Corr", ('IV', 'y')] = np.corrcoef(QA.loc['1':'11', ('IV', 'y')], QA.loc['1':'11', ('IV', 'x')])[0,1]

x = QA.values[0:11, 0].reshape(-1, 1)
y = QA.values[0:11, 1]

QA1_model = LinearRegression()
QA1_model.fit(x, y)

x_min = QA.values[0:11, 0::2].min()
x_max = QA.values[0:11, 0::2].max()
(x_min, x_max)
# gerar um conjunto de valores de x para predizer os valores de y
QA_x1_pred = np.linspace(x_min - 1, x_max + 1, 20).reshape(-1, 1)
# Aplique o modelo para previsões.
QA_y1_pred = QA1_model.predict(QA_x1_pred)


x = QA.values[0:11, 2].reshape(-1, 1)
y = QA.values[0:11, 3]

QA2_model = LinearRegression()
QA2_model.fit(x, y)


QA_x2_pred = np.linspace(x_min - 1, x_max + 1, 20).reshape(-1, 1)
QA_y2_pred = QA2_model.predict(QA_x2_pred)

x = QA.values[0:11, 4].reshape(-1, 1)
y = QA.values[0:11, 5]

QA3_model = LinearRegression()
QA3_model.fit(x, y)

QA_x3_pred = np.linspace(x_min - 1, x_max + 1, 20).reshape(-1, 1)
QA_y3_pred = QA3_model.predict(QA_x3_pred)


x = QA.values[0:11, 6].reshape(-1, 1)
y = QA.values[0:11, 7]

QA4_model = LinearRegression()
QA4_model.fit(x, y)

QA_x4_pred = np.linspace(x_min - 1, x_max + 1, 20).reshape(-1, 1)
QA_y4_pred = QA4_model.predict(QA_x4_pred)




plt.style.use('classic')

fig = plt.figure()
plt.plot(QA_x1_pred, QA_y1_pred, '-', label='QA1_model')
plt.plot(QA_x2_pred, QA_y2_pred, '-', label='QA2_model')
plt.plot(QA_x3_pred, QA_y3_pred, '-', label='QA3_model')
plt.plot(QA_x4_pred, QA_y4_pred, '-', label='QA4_model')



plt.figure()

# crie o primeiro dos dois painéis e defina o eixo atual
plt.subplot(2,2,1) # (rows, columns, panel number)
plt.plot(QA_x1_pred, QA_y1_pred, '-', label='QA1_model')

# crie o segundo painel e defina o eixo atual
plt.subplot(2,2,2)
plt.plot(QA_x2_pred, QA_y2_pred, '-', label='QA2_model')

# crie o terceiro painel e defina o eixo atual
plt.subplot(2,2,3)
plt.plot(QA_x3_pred, QA_y3_pred, '-', label='QA3_model')

# crie o quarto painel e defina o eixo atual
plt.subplot(2,2,4)
plt.plot(QA_x4_pred, QA_y4_pred, '-', label='QA4_model')

# Primeiro crie uma grade de gráficos
# ax será um array de dois por dois objetos Axes
fig, ax = plt.subplots(2, 2)
# Chama o método plot() no objeto apropriado
ax[0,0].plot(QA_x1_pred, QA_y1_pred, '-', label='QA1_model')
ax[0,1].plot(QA_x2_pred, QA_y2_pred, '-', label='QA2_model')
ax[1,0].plot(QA_x3_pred, QA_y3_pred, '-', label='QA3_model')
ax[1,1].plot(QA_x4_pred, QA_y4_pred, '-', label='QA4_model')

fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(x));



plt.figure()
plt.plot(x, np.sin(x))

plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.figure()
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported

plt.figure()
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.figure()
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted

plt.figure()
plt.plot(x, x + 0, '-g')  # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r');  # dotted red

plt.show()