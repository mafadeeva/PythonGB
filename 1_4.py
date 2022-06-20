n = int(input("Введите целое положительное число n: "))
max_num = n % 10
while n > 0:
    a = n // 10 % 10
    if max_num >= a:
        max_num = max_num
    else:
        max_num = a
    n = n // 10

print(max_num)