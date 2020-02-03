# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

number_user = int(input('Введи число: '))
check_number = 0
num = number_user
while num > 0:
    digit = num % 10
    if digit > check_number:
        check_number = digit
    num = num // 10
print (check_number)





