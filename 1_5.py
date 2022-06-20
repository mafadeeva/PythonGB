dohod = int(input("Введите значение выручки:  "))
rashod = int(input("Введите значение издержек: "))
if dohod >= rashod:
    print(f"Прибыль компании составила {dohod - rashod} рублей")
else:
    print(f"Убытки компании составили {rashod - dohod} рублей")
