import math
import time


def factorial_number_system(k, elements):
    n = len(elements)
    permutation = []

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        permutation.append(elements.pop(index))
        k %= fact

    return permutation


# 初始化數列
elements = list(range(32))

# 計算第 k 秒的排列
k = 0
while True:
    perm = factorial_number_system(k, elements.copy())  # 計算第 k 秒的排列
    print(perm)
    k += 1
    time.sleep(1)  # 等待 1 秒