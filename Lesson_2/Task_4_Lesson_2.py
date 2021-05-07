# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

while True:
    var_str = input('Пожалуйста введите несколько слов, разделяя их пробелами: ')
    if len(var_str) < 3 or var_str.count(' ') < 1:
        print('Неправильно введенные данные. Попробуйте еще раз')
        continue
    break

for idx, word in enumerate(var_str.split()):
    print(idx + 1, (word, word[:10])[len(word) > 10])

list_str = var_str.split()
for idx in range(len(list_str)):
    print(idx + 1, list_str[idx][:10])