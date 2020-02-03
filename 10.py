# Задача 10
# Найти количество цифр 5 в числе.
number = 12345678
temp = 0
while number > 0:
    if number % 10 == 5:
        temp += 1
    number=number//10
print(temp)
