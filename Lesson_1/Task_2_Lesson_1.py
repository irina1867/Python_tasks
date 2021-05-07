#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
# Используйте форматирование строк.

seconds = int(input())
# seconds = seconds % (3600 * 24)
hours = seconds // 3600
minutes = (seconds % 3600) // 60
clear_sec = seconds % 60
print(f'{hours:02d}:{minutes:02d}:{clear_sec:02d}')
