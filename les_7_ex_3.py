#Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

def median(array, first, second):
    array = array.copy()
    mid = len(array) // 2

    if first >= second:
        return array[mid]

    center = array[mid]
    i = first
    j = second

    while i <= j:
        while array[i] < center:
            i += 1
        while array[j] > center:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if mid < i:
        array[mid] = median(array, first, j)
    elif j < mid:
        array[mid] = median(array, i, second)

    return array[mid]

# Пока решал задачу пользовался функциями из предыдущей задачки, чтобы нагляднее было.
# def stick_together(first, second):
#     spam = []
#     i, j = 0, 0
#     while i < len(first) and j < len(second):
#         if first[i] < second[j]:
#             spam.append(first[i])
#             i += 1
#         else:
#             spam.append(second[j])
#             j += 1
#     spam.extend(first[i:] if i < len(first) else second[j:])
#     return spam
#
# def split_up(array):
#     x = len(array) // 2
#     first = array[:x]
#     second = array[x:]
#
#     if len(array) == 1:
#         return array
#     if len(array) == 2:
#         if array[0] <= array[1]:
#             return array
#         else:
#             return array[::-1]
#     else:
#         return stick_together(split_up(first), split_up(second))
#     return split_up(array)

MIN_SIZE = 1
MAX_SIZE = 10
#m = random.randint(MIN_SIZE, MAX_SIZE)
m = int(input('Введите переменную m для определения размера массива: '))

SIZE = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

median = median(array, 0, len(array) - 1)


print(f'Исходный массив размером 2*{m}+1 = {SIZE} элементов:\n{array}')

print(f'Искомая медиана: {median}')

# print(f'Упорядоченный массив:\n{split_up(array)}')