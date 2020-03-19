#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

# Ссылка на блок - схему:
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7Vxbj6M2FP410bYjTYVvQB4nc%2Bmu1GpXmkqdPlUk8SRUJE4J2Un219eAudpJmCbYJMwLgWNj7HP%2FDiYDdL%2FY%2Fhp6q%2FnvbEqDAbSm2wF6GEAIbAfxn5iySynu0E4Js9Cfik4F4dn%2FQQXREtSNP6XrSseIsSDyV1XihC2XdBJVaF4Ysrdqt1cWVJ%2B68mZUIjxPvECm%2FulPo7lYBXQK%2Bmfqz%2BbZk4E9TFsWXtZZrGQ996bsrURCjwN0HzIWpWeL7T0NYuZlfEnve9rTmk8spMuoyQ3rz%2FTuCx5%2FdZ9fv3z948tL%2BLe%2FvhXSWUe7bMF0ytcvLlkYzdmMLb3gsaCOQrZZTmk8qsWvij6%2FMbbiRMCJ%2F9Ao2glhepuIcdI8WgSilW796CW%2B%2FRcirv4qtTxsxcjJxU5cpPOMJ7d3%2BYK0ZptwQg%2BsGeTM51pL2YJG4Y7fF9LAi%2Fzv1fE9oT6zvF9%2B6zfm8ydDS6g6toWchaIDbFWHiLxwRiNxVyEnflKaRkFKpPcOSYoJf%2FeCjVjCgDNu%2BBAfR9aAs9d1snN%2BHCXHxwG0A86%2B0TjkZ7P4jKv%2B5KefZbUIAm5ysfjf5n5En1dewuM3bvVV4Ypp0DCi28OikkWQsdKqsjKzoLfCAEFGm5eMz7X2C63C7vfylvTQSrAWK4GarQSrrSQ5jqCwifiI4zkNIH%2BKNU5%2FJpIScI%2B%2Bik85e70goAGbhd6CS2FFQ59PlIb1tm9FgwEzyj3SMTuy27Ijp4d2ZGuxI0T02tHQpCRBSY6FVC9UkgTXPGI9irUsSVvyiNzRWcmZ9cn6JMk5nLPFeLPW48HgnmhR8mCuzkTAVYcPLBKrOq%2F4yqMqU7zAny35%2BYRzIAkDMX98nnPdiYaFP52m1kLX%2Fg9vnAwVK%2FIqVoBkPWQ0IA%2FxWNxA1qmtnInfBOAqv4cyv5GC37AtfgMg8fT6%2FQyw1EI60dHYrllHkyF6Re7FsclIlYHVsQn%2F%2FXfDkrPC7B5jdxUPAUpDuGKIAvA8ZHTe86k00IUldVK4IKaTOgDVcr0ryTJlPkmYb8smrRFbSlbQNCluLaYApOZfmWfw4kNLPZQjBajHOkMLlHmqE4wYCi0ivqeu%2FlBH98QYdJpssFHZGCpL6qm44HogaDvsyyWXcQ4w5JTZJLxAiliqFV4AGYxdFb5Aw5ouWobxBezQ%2Bw%2FroKPhHA53L%2BWLUuiIL4vbkqs2HJTbNHiYjB1AgdEFkHhlsYvLoUSJVlKADBjEDbep%2Bt%2FxDgCutmXUIEZpBGD4OlSPruCahLJeecsmk3GVcylTsuemI57wlFSHrKTp1Vv4wS5t5Hd5i1XSiBDmvxO2XLOAi7PeoOZaAQnSl1Gcg%2FfJuZMhNKsE4fJuOYSD4hZYRndWGlLOt%2Fr%2FzWNJ5JeFMmENJSHbNMqERB0arwwl1ZM1ZBglIbMB8h0oKQ%2BQwFiAzDaFHA2QcGgyQmbTVJf8B3DUraI%2FVvgerVk5MotGL8wGhg1tABnNErNplmzAS7KaONkZy%2FpfkaaG%2BFuPA47p%2BIs6tAem80gJZTsVO42UslleGFIqvwF6zLBAPmCWCSZTqZh0PXOX4deFJ%2B0AdM5pQHXSfq31LAIM17OQ4uXaZRfOW6%2BHE6cmjD318OMD1bcypmGitcI6ktP4HiBionhfqxcRy%2FXFEnq67RZ2IooQoBc7Gd0o2C3sdDQbxC15vJpS2ECvo8JyoO%2BtDhzfdt9YWeCJynKSXWMZO8TJ9m0n0TNxTSfC%2BPJKSObQM4YNTaAdd1l79dFwu8RdGHq7UjeRGzV%2BCqh9vNdoUoVKpo8%2Fr9tWgLfrKw%2Fc9rQ40AGfuGff47UWB2zFjketxQH8URx4b3HAbrhH%2FvhA9e%2Bz2s65e1kcsBUb%2BLQWB%2FDB4sBNt4oDtiIEaC0O4I%2FiQPPiANFTHHDqttGyoyJyoO%2BtDhxFRqSxshgtDhB1ceCmk8UBW%2FGNo95EmFxMceCcqnyqhu5xZ5YSKJ8bvWP9cJz0Ao7f9BSOd8AL9QyOO4qttVrhOOnQjqoLgePO8Exw3KmbUdtZ7p4Pu64bjjuKnbta4Tg5stP5qVuA3FEEAa2AnLhGXVKnwNhRjJUqd%2BuA3EWaXdVHUeYdfwllNVUWo4A8m6a02%2F2pk5DcVXwWrDcZto3%2B75AhSH6yjnYJkmduc29GeAjBN11Dq4Df7gXgz31Q7yB%2FB7xczyC%2Fq9g7fCbIzy%2BLf%2FJOPUDxf%2Bjo8T8%3D

def calc():
    print("Калькулятор устроен следующим образом: введите первое число, второе число и знак операции \n 1. сложение: '+' \n 2. вычитание: '-' \n 3. умножение: '*' \n 4. деление: '/' \n для выхода из калькурятора введите '0'")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = str(input("Введите знак операции: "))
    while c != 0:
             if c == '0':
                print('\n**\nСпасибо за внимание\n**\n')
                break
             elif b == 0.0:
                print('\n**\nЗдесь нельзя делить на 0, попробуйте другое число\n**\n')
                calc()
             elif c == '+':
                print('\n**\nОтвет: ', a, c, b, ' = ', a + b, '\n**\n')
                calc()
             elif c == '-':
                print('\n**\nОтвет: ', a, c, b, ' = ', a - b, '\n**\n')
                calc()
             elif c == '*':
                print('\n**\nОтвет: ', a, c, b, ' = ', a * b, '\n**\n')
                calc()
             elif c == '/':
                print('\n**\nОтвет: ', a, c, b, ' = ', a / b, '\n**\n')
                calc()
             else:
                print('\n**\nЧто-то пошло не так, проверьте правильность введения знака\n**\n')
                calc()
print(calc())

