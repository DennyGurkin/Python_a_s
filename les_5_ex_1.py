# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

Company = collections.namedtuple('Company', ['q1', 'q2', 'q3', 'q4'])

user_company = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль в первом квартале: '))
    profit_q2 = int(input('Прибыль во втором квартале: '))
    profit_q3 = int(input('Прибыль в третьем квартале: '))
    profit_q4 = int(input('Прибыль в четвертом квартале: '))
    user_company[name] = Company(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )

total_profit = ()

for name, profit in user_company.items():
    print(f'Годовая прибыль компании {name} составила: {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(user_company)
print(f'Среднегодовая прибыль всех компаний составила: {avg_profit_total}')

print('Предприятия с прибылью выше средней:')

for name, profit in user_company.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} (прибыль составила {sum(profit)})')

print('Предприятия с прибылью ниже средней:')
for name, profit in user_company.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} (прибыль составила {sum(profit)})')
