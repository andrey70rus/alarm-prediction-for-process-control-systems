import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

y1 = np.array(genfromtxt('out_validation_pred.csv', delimiter=',', max_rows=50))
y2 = np.array(genfromtxt('out_validation.csv', delimiter=',', max_rows=50))

x = np.linspace(0, 50, 50)

fig, ax = plt.subplots()
graph1 = plt.plot(x, y1, color='blue', label='Модель', linestyle='--')
graph2 = plt.plot(x, y2, color='red', label='Истинное значение', alpha=0.5)
ax.set_ylabel("Расход")
ax.set_xlabel("Номер предсказанного значения")
ax.legend()
plt.show()