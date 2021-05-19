# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, str(year), city, email, telephone])


name_ = input('your name')
surname_ = input('enter surname')
year_ = int(input('enter year'))
city_ = input('enter city')
email_ = input('enter email')
telephone_ = input('input telephone')

print(my_func(
    city=city_,
    surname=surname_,
    name=name_,
    year=year_,
    email=email_,
    telephone=telephone_))
