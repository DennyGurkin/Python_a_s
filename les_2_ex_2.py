# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#Ссылка на блок - схему:
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=les_2_ex_2.drawio#R7Rprj5s48NfwcSvAQJKPy256PalVK%2B1J136qvMEL9CDmHGcT%2ButvjE14mGRZpUCyPSki9vjBeN4zxkB36f4PhrPoEw1IYthmsDfQvWHblmPbhviZQS4hMwtJQMjiQE2qAA%2FxT6KApoJu44BsGhM5pQmPsyZwRddrsuINGGaM7prTnmjSfGuGQ6IBHlY40aF%2FxwGPJHRuzyr4BxKHUflmy1vIkRSXk9VJNhEO6K4GQksD3TFKuWyl%2BzuSCOKVdJHr3h8ZPSDGyJr3WbDKn8wff33G%2BZ%2Fh8uvn788fP%2F3z4UZxZ8Pz8sAkgPOrLmU8oiFd42RZQX1Gt%2BuAiF1N6FVzPlKaAdAC4A%2FCea6YibecAijiaaJGyT7mX8Xyd67qfauN3O%2FVzkUnVx2Jp0Du6PEVaEO3bEVOnLkUI8xCwk%2FMQwcmgXQTmhLOcljHSIJ5%2FNzEAysxCw%2FzDku%2F0BgwtE2lEk4p2XmpImZzC4mXWlXxExo1NCpQweVXcFwh%2FIyTrTqCAQRe3IunbxrAhvmsbMPTL55LXUySBFRQiMMuijl5yHBB8x1YgSaz1esI42R%2FmnU6qdUC5DZJVmrUrlJIq4RFNWWcm8eZ0yDra2mIumlYPH1bUUw8HcP2EsDGf2TQCkULa6QEw5CJJhAEJwlJaMhwCjMzwmLAl7D22JdqYALqHwT2JfJ7Q5HffWtG69cbGXPxzm3qTE8z02crs7WVtLiDWazZlOy2asyuWD%2B4j%2FKGEYtFU5Xdxbi%2BBy0m1dxXsBIYxvID%2F0Wntkp0q2VFbygR6BGmWOfKylm22NNdoXJ5GSMNVnv%2FbkWo6z%2FRNb95wmmcANFuDeE5PJxmBfEQcuAfYvkNTQDV9kC1Sc2bwnqwT6bAQrxHvEoYKIkEnKnAQ87WpI9FNH3cbsbxo7OW8rm6H52PGcXMO6MYX0aCbhEJ6ukBnJ83SYOTOFxDewV0KEISQaUYMqhbNZDGQSA1mWzin%2Fix2EooSybsTHEq1zfce7EXKO9G6vEvorrTil48U6c66qC6PRTVy%2FC%2FTXZHBd3XTnBUGvmLIfjV5LgHp1PzM98abuZcp%2FOiMxko7mjlvC4aN4JE3v8i0L880ldWzs5dzlNrvZCBVQgAK4UctTPv%2FenhvDncjhQa0jB%2B1o06ooVxs240qR2dKA%2Bz3EEMoudNm4hZrqY8lfgXLdu3NHaPrQNauupNrQOOTpTJHInZ05FMlsBavTPYaR2JnsJWnmJ%2FKbpwKLpdjC7Yzm%2FoDwaq17ot7joj%2BwP7SDBVFmBU9cTU09MpKyjO1BUU%2B3csTdvD5IjtkGh0FeioZKpLPcuY%2B51Xe1I51o8bWaRsZxQlRFQ8jaOlUFl%2BEYXQWbbXK5w1CLz2dtaozql6nUQQnqIQeiPd1p3Q33Y9r9%2FqvIFFWUeVpzhSSL3wO8x2JOlM7z27q6%2BL25qI1TnXUcEY8QZeU86%2B2ehgpte5mmz0Aq6SkPpg4cIjcaR%2FV1GVdGQ88h5%2BVkcUMnI0ruXvk9sTNOu2J2%2F7NqfLjjsdZB%2FscgEdMeNv5janfWmJdIKPepvjTJp1Xlkp37kOu%2B%2BcsvsvlPLNU4X86R2F9unigB%2FPQbf6mlimRdU32Wj5Hw%3D%3D

a = int(input("Введите любое натуральное число: "))
x = 0
y = 0
while a > 0:
    if a % 2 == 0:
        x += 1
    else:
        y += 1
    a = a // 10


print("Во введенном числе четных цифр - {}, нечетных цифр - {}".format(x, y))

