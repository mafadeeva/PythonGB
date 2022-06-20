dohod = int(input("Введите значение выручки: "))
rashod = int(input("Введите значение издержек: "))
if dohod >= rashod:
    rent = (dohod - rashod)/dohod
    chisl = int(input("Введите численность сотрудников: "))
    ud_prib = (dohod - rashod)/chisl
    print(f"Прибыль компании составила {dohod - rashod} рублей,\n"
          f"рентабельность составила {rent*100:.1f} процентов,\n"
          f"удельная прибыль составила {ud_prib:.1f} рублей на человека.")
else:
    print(f"Убытки компании составили {rashod - dohod} рублей")