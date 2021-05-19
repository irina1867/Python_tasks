# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(arg1, arg2, arg3):
    l = [arg1, arg2, arg3]
    l.sort(reverse=True)
    return sum(l[:2])


print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')