#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int (input('Размер выручки за текущий месяц: '))
costs = int (input('Размер издержек за текущий месяц: '))
if revenue > costs:
    print ('Этот месяц с прибылью')
    print ('Рентабельность: ', (revenue - costs) / revenue )
elif revenue < costs:
    print ('В этом месяце убытки')
num_of_empl = int (input('Введите численность сотрудников: '))
empl_profit = (revenue - costs) / num_of_empl
print('Размер прибыли на одного сотрудниука: ', empl_profit)
