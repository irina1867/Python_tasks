#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count

end = int(input('введите конечное число: '))
for el in count(int(input('Введите стартовое число '))):
    print(el)
    if el < end:
        continue
    else:
        break

print('ВСЁ!')