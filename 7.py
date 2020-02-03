# Задача 7
# Найти произведение цифр числа.

number=918273645
sum=1
while number>0:
    sum*=number%10
    number=number//10
print(sum)