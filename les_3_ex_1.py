# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [i for i in range(2, 100)]
b = [i for i in range(2, 10)]
c = []

x = 0
while x < len(b):
    for i in range(0, len(a)):
        if a[i] % b[x] == 0:
            c.append(a[i] % b[x])
    x += 1
    y = len(c)
    print('Чисел, кратных {}: {} '.format((x+1), y))
    c = []