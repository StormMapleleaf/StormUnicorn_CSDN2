import math

for num in range(2, 101):
    is_ss = True
    x = int(math.sqrt(num)) + 1
    for i in range(2, x):
        if num % i == 0:
            is_ss = False
            break
    # 如果is_prime仍然为True，则num是素数
    if is_ss:
        print(num)
