# Цикл While

# Простейший While

i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5: break

answer = None
while answer != "Volvo":
    answer = input("Какая марка автомобиля?")
print("Вы правы!")

while i < 10:
    print(i)
    i = i + 1
    if i == 9: break
    if i < 3: continue