# Задача 9
# Найти максимальную цифру в числе.

number = 2345469
temp=0
while number>0:
    if number%10>=temp:
        temp =number%10
    number=number//10
print(temp)