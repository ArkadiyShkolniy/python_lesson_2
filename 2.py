# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

sum=0
for i in range(10):
    answer = int(input('Введите любую цифру'))
    if answer==5:
        sum+=1
print('Количество цифр пять:', sum)
