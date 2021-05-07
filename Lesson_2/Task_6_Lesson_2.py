# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products, order = [], 1
title, price, amount = None, None, None


q = 'N'

while q not in ['Y', 'y']:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue
        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числомю. Попробуйте еще раз.')
            continue
        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue

    unit = tmp

    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)
    q = input('Формирование списка завершено? (Y/N)) ')




for item in products:
    temp_title = item[1]['title']
    temp_p = item[1]['price']
    temp_a = item[1]['amount']
    temp_u = item[1]['unit']
    print(f'{item[0]} \t {temp_title} \t {temp_p} \t {temp_a} \t {temp_u}')

