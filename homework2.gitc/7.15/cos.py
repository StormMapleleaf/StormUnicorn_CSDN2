# 求解 x=cos(x)
import math
def fun():
    x = 1
    while abs(math.cos(x) - x) > 1e-10:
        x = math.cos(x)
    return x
print(fun())