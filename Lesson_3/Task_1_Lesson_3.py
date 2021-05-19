# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"


print(my_func(input("Enter x = "), input("Enter y = ")))