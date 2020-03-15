#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# C числами типа 1234, 435, 42 работает хорошо. Но вот когда вводится 1230, например, последний нолик (он же первый после рекурсии) отваливается..Не нашел культурного способа это поправить.:(

#Ссылка на блок - схему:
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=les_2_ex_3.drawio#R5Vrdb6M4EP9b7oGXk%2FZkMB%2FJY2m6e9LdSSt1dbd9dIJLWBnMGadJ9q9ffxEwkKZVC7S7UkTs8dd4Zn5jz4ADr%2FPDJ4bK7T80wcTxQHJw4MrxPNf3PEf%2BQHLUlMiFmpCyLDGdGsJt9h0bIjDUXZbgyurIKSU8K23ihhYF3nCLhhije7vbPSX2qiVKcY9wu0GkT%2F0vS%2FhWUxde1ND%2FxFm6rVd2w6VuyVHd2eyk2qKE7lskeOPAa0Yp16X8cI2JFF4tFz3u45nWE2MMF%2FwpA77AMrj7d%2BXC1d1ft%2Fx%2BX%2B34wwejnYof6w3jROzfVCnjW5rSApGbhhozuisSLGcFotb0%2BZvSUhBdQfyGOT8aZaIdp4K05TkxrfiQ8a9y%2BB%2BBqd21WlYHM7OqHE1F8ymZO7t9Q6rojm3wI3uuzQixFPNH%2BsGTkoR1Y5pjzo5iHMME8ezB5gMZM0tP%2FU5DP9NMcOgBAwnf9fWQYw0RYE%2Bh%2BTKjGn2KQouNhqS0%2FAyNG4YfENmZLThCwMuVfMbAEWpYRHVZPGP1vOmbCSECgtIc9tuM49sSKZnvhRewlW2Ww4zjw%2BOq64vaDICBLbIaUfsGkG5N27bAuADnlWOJ9bky9H9B1EyDBm9iNMBhNKhn7Bnbl09f8tRTu%2FDppSwKgSJCMKEpQ7mQe4lZJljDrNv2uWmYATgnX3MJOeFYyAl%2FQeQEkyDHnxg5QQ85Ah4hyqUVF%2BuqVDIEqgUoFkIi5BavmSilqmQ3d8zCVvr0UIFwbqgs5oSK2wJKA5vRoRKNApUAABsq3YvB2FcuMKcqZ%2FJ646iy6%2FWCaFpVRkNeD%2Fym%2FVhfzWxL8%2FWumsaDRWcOhJYHW0x5S14O3610pBGoSKMffor9c1s0iGRpIcobIQd1b5JSykSEfmUa8ixJNGRwlX1HazWVtOZSWoHaVRA7wUrOJVBSacC8ktT9zrnhB32p%2BwNS98aSunsmwPNNUPfeBd4182AgGoRTCvzkEd%2F8QS0kzI5f25XWKFlthqnaGLkXg%2FiLyRd3%2BcLz42Ug8oZB5CmvFQ9Gh%2BueGbzx6NBfXnZd01553YFw3MQNJcOWcMP%2FdzJxGt%2FTgn%2B4R3lGxC6uZEhRByGOuMP74n9Di4oSwWu3oZmkDknqxeSk51fT%2Fkyu5brloT9LE9ggxU8gewJVjLWdgN8NSS8nZKVXtLkQZLXrmvrGIqTT1Ws%2Bc5k3m%2FDOPK%2F%2FRM%2F7KumKK8bQsdXB3AzO3uuha4doEQja5nGxPwxBx5w0B68bx%2Fk%2Fg3tCHff0Uf3evTsKo2BudxTM4Y6e6iJGCMXhsAIuhOKXJ4IdDWnfNl56ZtZM23PSM80x0pwcd9bBMf4xEk10jLwMiv08TXMrG0jTzOy7vNnfy7hnkjVXrSCnnbgZuHlN%2BEI4DO3TfyjV9VpvhEW1%2BUZDu5zmSxd48wM%3D

def revers(a, b):
    while a != 0:
        b = a % 10 + b * 10
        a = a//10
        revers(a, b)
    return b

print(revers (int(input("Введите любое натуральное число: ")), 0))
