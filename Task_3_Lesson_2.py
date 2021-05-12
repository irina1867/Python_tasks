# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons_list = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]
seasons_dict = {
    'Зима': ['12', '1', '2'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}
while True:
    month_number = input('Пожалуйста введите номер месяца: ')
    is_find = 0
    for season in seasons_dict.keys():
        if month_number in seasons_dict[season]:
            is_find = 1
            break
    if is_find == 0:
        print('Неправильно введенный номер месяца. Попробуйте еще раз')
        continue
    break
for season, months in seasons_list:
    if month_number in months:
        print(f'Через список определено, что месяц с номером {month_number} это {season}')
for season, months in seasons_dict.items():
    if month_number in months:
        print(f'Через словарь определено, что месяц с номером {month_number} это {season}')

# 2021-05-12 change