# Динамическая типизация
#
temp_var_1 = input("Input Something")
print(temp_var_1, type(temp_var_1), id(temp_var_1))

temp_var_2 = input("input something again")
print(temp_var_2, type(temp_var_2), id(temp_var_2))

#temp_var_1 = temp_var_2
temp_var_1 = int(temp_var_2)
print(temp_var_1, type(temp_var_1), id(temp_var_1))

# Приведение типов
temp_float = input("Input float number")
print(temp_float, type(temp_float), id(temp_float))
if temp_float. isdigit():
    temp_float=float(temp_float)
    print(temp_float, type(temp_float), id(temp_float))
else: print("there is not number")