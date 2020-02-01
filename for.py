# Циклы For

# Простейший цикл For
for i in range(10): # range (start, stop, step)
    print(i)
    if i == 5: break
for i in range(5):
    answer = input ("Какая марка авто?")
    if answer == "Volvo":
        print("Вы правы")
        break

for i in range(10):
    if i == 9: break
    if i < 3: continue
    else: print(i)