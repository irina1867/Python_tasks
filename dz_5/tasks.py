


# Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере рулетки или подбрасывания монетки.
# Сгенерируйте десять выборок случайных чисел х0, …, х9.
# и постройте гистограмму распределения случайной суммы  +х1+ …+ х9.

from random import choice
import numpy as np
import matplotlib.pyplot as plt

event_dict = {}
for j in range(100000):
    event_list = ''
    for i in range(3):
        event = choice(['О', 'Р'])
        event_list += event
    if event_list in event_dict:
        event_dict[event_list] += 1
    else:
        event_dict[event_list] = 1

print(event_dict)


list_sum = []
for j in range(1000):
    list_random = []
    for i in range(10):
        list_random.append(np.random.randint(1, 10))
    print(list_random)
    list_sum.append(sum(list_random))

# print(list_sum)
n, bin, patches = plt.hist(list_sum, bins=10)
plt.show()
