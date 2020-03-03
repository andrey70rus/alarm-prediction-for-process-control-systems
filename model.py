from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import pandas as pd

in_data_train = np.array(genfromtxt('in.csv', delimiter=','))
out_data_train = np.array(genfromtxt('out.csv', delimiter=','))
in_data_test = np.array(genfromtxt('in_validation.csv', delimiter=','))
out_data_test = np.array(genfromtxt('out_validation.csv', delimiter=','))
# Среднее значение
mean = in_data_train.mean(axis=0)
# Стандартное отклонение
std = in_data_train.std(axis=0)
in_data_train -= mean
in_data_train /= std
in_data_test -= mean
in_data_test /= std

# Создание НС
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(in_data_train.shape[1],)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Обучение НС
model.fit(in_data_train, out_data_train, epochs=5, batch_size=1, verbose=2)

# Проверка корректности предсказания
pred = model.predict(in_data_test)

# for i in range (0,len(pred)):
#     print("Прогнозируемое значение:", pred[i][0])

# frame = pd.DataFrame(pred)
# frame.to_csv('out_test22.csv', index=False)