# Задача 6
# # Найти сумму цифр числа.

number=1029384756
sum=0
while number>0:
    sum+=number%10
    number=number//10
print(sum)