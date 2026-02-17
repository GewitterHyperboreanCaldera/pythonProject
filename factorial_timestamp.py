import math

import time
current_time = time.time()  # 這裡返回的是普通整數
print(current_time)

def decimal_to_factorial(n):
    """將十進制數轉換為階乘進制"""
    i = 1
    res = []
    while n > 0:
        res.append(n % i)
        n //= i
        i += 1
    return res[::-1]



def factorial_to_decimal(factorial_list):
    """將階乘進制轉回十進制"""
    return sum(d * math.factorial(i) for i, d in enumerate(reversed(factorial_list)))

timestamp = int(time.time())

# 以當前 Unix 時間戳為例
factorial_representation = decimal_to_factorial(timestamp)
print("階乘進制表示:", factorial_representation)

# 289966101*3 =
#
# 869898303

#
# 72491525

#
# 14498305

#
# #2416384
#
# #345197

recovered_timestamp = factorial_to_decimal(factorial_representation)
print("還原回 Unix 時間戳:", recovered_timestamp)