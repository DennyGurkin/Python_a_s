# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(0, SIZE)]

print("\nИсходный массив случайных чисел:\n{}".format(a))

i = 0
index = 1
while i < len(a):
    if a[i] < 0 and index == 1:
        index = i
    elif a[i] < 0 and a[i] > a[index]:
        index = i
    i += 1

print("\nМаксимальный отрицательный элемент в массиве: {}\nПозиция в массиве: {}".format(a[index], index + 1))
