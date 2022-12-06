 # Импортируем необходимые пакеты
import numpy as np
import time

start_time = time.time()

# Зададим обучающую выборку
m = 17
h = 2

eps = 0.000001

dataX = [
    [0.1, 0.2, 0.3, 0.4],
    [0.2, 0.3, 0.4, 0.5],
    [0.3, 0.4, 0.5, 0.6],
    [0.4, 0.5, 0.6, 0.7],
    [0.5, 0.6, 0.7, 0.8],
    [0.6, 0.7, 0.8, 0.9],
    [0.7, 0.8, 0.9, 0],
    [0.8, 0.9, 0, -0.1],
    [0.9, 0, -0.1, -0.2],
    [0, -0.1, -0.2, -0.3],
    [-0.1, -0.2, -0.3, -0.4],
    [-0.2, -0.3, -0.4, -0.5],
    [-0.3, -0.4, -0.5, -0.6],
    [-0.4, -0.5, -0.6, -0.7],
    [-0.5, -0.6, -0.7, -0.8],
    [-0.6, -0.7, -0.8, -0.9],
    [-0.7, -0.8, -0.9, 0]
]

dataY = [1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 0, -1, -1.2, -1.3, -1.4, -1.5, -1.6, -1.7]

print('Задаем обучающую выборку')
print('Функция активации 1/(1+exp(-x))')


def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))
    return sig


def diffsig(x):
    # Запишите выражение для производной для функции активации сигмоида
    sigm = sigmoid(x)
    diffsig = sigm * (1 - sigm)
    return diffsig


# Инициализируем веса
w1 = 0.1
w2 = 0.2
w3 = 0.3
w4 = 0.4
print('0 этап алгоритма. Инициализируем веса')


# Функция потерь
def loss_func(w1, w2, w3, w4, dataY, dataX, m=17):
    E = 0
    for i in range(m):
        E += (dataY[i] - sigmoid(w1 * dataX[i][0] + w2 * dataX[i][1] + w3 * dataX[i][2] + w4 * dataX[i][3])
              ) * (dataY[i] - sigmoid(w1 * dataX[i][0] + w2 * dataX[i][1] + w3 * dataX[i][2] + w4 * dataX[i][3]))
    return E


# Вычисляем значение функции потерь
loss_new = loss_func(w1, w2, w3, w4, dataY, dataX)
print('1 этап алгоритма. Вычисляем значение функции потерь. E(w1,w2,w3,w4) = ', round(loss_new, 6))


# Производная функции потерь по jму весу
def diff_loss_func(j, w1, w2, w3, w4, Y, X):
    diffE = 2 * (Y - sigmoid(w1 * X[0] + w2 * X[1] + w3 * X[2] + w4 * X[3])
                 ) * diffsig(w1 * X[0] + w2 * X[1] + w3 * X[2] + w4 * X[3]
                             ) * X[j]
    return diffE


# Вычисляем значение градиента функции потерь
print('2 этап алгоритма. Вычисляем значение градиента функции потерь. diffE(w1,w2,w3,w4) = (',
      round(diff_loss_func(0, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      round(diff_loss_func(1, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      round(diff_loss_func(2, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      round(diff_loss_func(3, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      ')')

# Вычисляем изменение весов
print('Вычисляем изменение весов. Шаг алгоритма h=', h, '. divW = (',
      round(h * diff_loss_func(0, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      round(h * diff_loss_func(1, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      round(h * diff_loss_func(2, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      round(h * diff_loss_func(3, w1, w2, w3, w4, dataY[0], dataX[0]), 6),
      ')')

# Корректируем веса
w1 = w1 + h * diff_loss_func(0, w1, w2, w3, w4, dataY[0], dataX[0])
w2 = w2 + h * diff_loss_func(1, w1, w2, w3, w4, dataY[0], dataX[0])
w3 = w3 + h * diff_loss_func(2, w1, w2, w3, w4, dataY[0], dataX[0])
w4 = w4 + h * diff_loss_func(3, w1, w2, w3, w4, dataY[0], dataX[0])

print('3 этап алгоритма. Корректируем веса W = (',
      round(w1, 6),
      round(w2, 6),
      round(w3, 6),
      round(w4, 6),
      ')')

# Запускаем цикл градиентного спуска
count_stop = 0
index = np.arange(17)
t = 0
for k in range(4000):
    # Познакомиться с функцией shuffle можно в документации
    # https://docs.scipy.org/doc/numpy-1.9.1/reference/generated/numpy.random.shuffle.html
    np.random.shuffle(index)
    loss_old = loss_new

    # Функция shuffle перемешивает нашу обучающую выборку.
    # Реализуйте этап изменения весов модели методом стохастического градиентного спуска.
    # На каждом шаге изменяйте веса, вычисляя производные, только для одного элемента обучающей выборки. 
    # После прохождения всех элементов, выборку нужно перемешать.
    ???
        ???
        ???
        ???
        ???

    loss_new = loss_func(w1, w2, w3, w4, dataY, dataX)
    if abs(loss_new - loss_old) < eps:
        count_stop += 1
    else:
        count_stop = 0
    if count_stop == 10:
        break
    else:
        print(t + 1, 'я итерация алгоритма. Вычисляем значение функции потерь. E(w1,w2,w3,w4) = ',
              round(loss_new, 6))
        t += 1

print("--- %s seconds ---" % (time.time() - start_time))

# Внесите значение loss_new на платформу
print(loss_new)