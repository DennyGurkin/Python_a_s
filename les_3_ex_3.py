# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(0, SIZE)]

# Вариант 1.
print("\nИсходный массив случайных чисел:\n{}".format(a))
x = 0
y = 0
for i in range(len(a)):
    if a[i] < a[x]:
        x = i
    elif a[i] > a[y]:
        y = i
print("\nМинимальное число в массиве: {}\nМаксимальное число в массиве: {}".format(a[x],a[y]))
b = a[x]
a[x] = a[y]
a[y] = b
print("\nМассив после перемены максимального и минимального числа:\n{}".format(a))

# Вариант 2.
# В процессе тестирования оказалось, что алгоритм работает, но почему-то иногда сбоит и не отрабатывает перестановку. Пришлось перейти к варианту 1.

# c = []
#
# print("Исходный массив случайных чисел:\n{}".format(a))
#
# max_a = a[0]
# for i in range(1, len(a)):
#     if a[i] > max_a:
#         max_a = a[i]
#     c.append(max_a)
# print("Максимальное число в массиве: {}".format(max_a))
#
# min_a = a[0]
# for i in range(1, len(a)):
#     if a[i] < min_a:
#         min_a = a[i]
#     c.append(min_a)
# print("Минимальное число в массиве: {}".format(min_a))
#
# a[a.index(min_a)], a[a.index(max_a)] = a[a.index(max_a)], a[a.index(min_a)]
#
# print("Массив после перемены максимального и минимального числа:\n{}".format(a))

