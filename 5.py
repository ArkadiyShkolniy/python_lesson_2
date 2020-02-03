# Задача 5
# Вывести цифры числа на каждой строчке.

integer_number = 33211

print(integer_number%10,integer_number//10)

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10