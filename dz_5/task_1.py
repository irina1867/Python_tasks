# Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).

from random import choice
import numpy as np
number = np.random.randint(0, 36)
color = choice(['red', 'black'])
if number != 0:
    print(number, color)
else:
    print('Zero!')