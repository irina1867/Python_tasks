# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    try:
        return float(x) ** int(y)
    except ValueError:
        return "enter only number"


def my_func2(x, y):
    try:
        ans = 1
        for i in range(-int(y)):
            ans /= float(x)
        return ans
    except ValueError:
        return "enter only number"


a = input("Enter x = ")
b = input("Enter y = ")
print(my_func(a, b))
print(my_func2(a, b))
