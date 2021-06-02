import numpy as np
k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)

x = a+b+c+d+e

for i in range(n):
    if x[i] == 3:
        k += 1

print(k, n, k/n)
print('теория', 10/32)
