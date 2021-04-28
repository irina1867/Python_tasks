# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while
# и арифметические операции
print("Введите ваше число")
n = int(input())
numb = n
max = n % 10
if n < 10:
    print(n)
else:
    while n >= 1:
        n = n // 10
        if n % 10 > max:
            max = n % 10
        if n > 9:
            continue
        else:
            print(max)
            break