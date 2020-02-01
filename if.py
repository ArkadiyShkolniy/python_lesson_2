# Оператор условия

brand = "Volvo"
engine_volume = 1.5
horsepower = 1222
sunroof = True

# Проверка условия If
#
# if horsepower < 80:
#     print("No tax")

# Проверка уловия If \ Else

# if horsepower <80 : print("No tax")
# else: print('Tax')

# Проверка условия If/elif/elif/else
tax = 0
if horsepower <80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else:
    tax = 50000
print(tax)

# Проверка условия If для присваивания

cool_car = 0
cool_car = 1 if sunroof == 1 else 0
print(cool_car)