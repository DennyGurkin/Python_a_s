# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(0, SIZE)]

print(a)

b = a[0]
rep_max = 1
for i in range(len(a) - 1):
    rep = 1
    for x in range(i + 1, len(a)):
        if a[i] == a[x]:
            rep += 1
    if rep > rep_max:
        rep_max = rep
        b = a[i]

if rep_max > 1:
    print('число {} в повторяется {} раз'.format(b,rep_max))
else:
    print('повторяющихся элементов нет')