# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(0, SIZE)]

print("\nИсходный массив случайных чисел:\n{}".format(a))
x = 0
y = 0
for i in range(len(a)):
    if a[i] < a[x]:
        x = i
    elif a[i] > a[y]:
        y = i
print("\nМинимальное число в массиве: {}\nМаксимальное число в массиве: {}".format(a[x],a[y]))

sum = 0
for i in range(x + 1, y):
    sum += a[i]
print("\nСумма элементов, находящихся между минимальным и максимальным элементами:\n{}".format(sum))
