#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и
# 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

lng =int(input("Введите количество элементов списка: "))
i = 0
user_list = []
helper = 0
while i < lng:
    user_list.append(input("Введите элемент списка"))
    i += 1
i = 0
print(user_list)
for helper in range(int(len(user_list)/2)):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i += 2
print(user_list)




