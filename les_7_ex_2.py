# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, з аданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

def stick_together(first, second):
    spam = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            spam.append(first[i])
            i += 1
        else:
            spam.append(second[j])
            j += 1
    spam.extend(first[i:] if i < len(first) else second[j:])
    return spam

def split_up(array):
    x = len(array) // 2
    first = array[:x]
    second = array[x:]

    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] <= array[1]:
            return array
        else:
            return array[::-1]
    else:
        return stick_together(split_up(first), split_up(second))
    return split_up(array)


print(f'Исходный массив:\n{array}')
print(f'Упорядоченный массив:\n{split_up(array)}')
