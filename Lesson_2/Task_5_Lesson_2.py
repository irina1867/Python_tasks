# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.

score_list = [7, 5, 3, 3, 2]  # Заводим список с местами, наш "рейтинг"
user_place = int(input('введи число'))  # тут мы получаем цифру от пользователя
score_list += [user_place]
score_list.sort(reverse=True)
# for i in range(len(score_list)):  # это цикл, которым мы сравниваем каждый i-й элемент с числом пользователя
#     if score_list[i] == user_place:  # это проверка числа пользователя с элементом на равенство. Если равны,
#         score_list.insert(i+1, user_place)  # пользовательское вставить послетакого же элемента, и спрыгнуть из цикла.
#         break
#     elif score_list[0] < user_place:  # проверяем 0-й элемент списка, если меньше пользовательского - вставляем первым.
#         score_list.insert(0, user_place)
#     elif score_list[-1] > user_place:
#         score_list.append(user_place)  # Если последний элемент списка > нашего числа -> добавляем число в конец списка
#     elif (score_list[i] > user_place) and (score_list[i+1] < user_place):
#         score_list.insert(i+1, user_place)
print(f"обновленный список: {score_list}")