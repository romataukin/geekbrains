#Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

enter_seconds = int (input('ввод секунд:'))
hours = enter_seconds//3600
minutes = enter_seconds%3600//60
seconds = enter_seconds%3600%60
print('%02d:%02d:%02d' % (hours, minutes, seconds))