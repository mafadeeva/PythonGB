name = input("Введите имя: ")
surname = input("Введите фамилию:  ")
day = int(input("Введите число рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))
if month <= 5 and day <= 14:
    age = 2022 - year
else:
    age = 2021 - year

print (f"Меня зовут {name} {surname}.")
print ("Мне %d." %(age))