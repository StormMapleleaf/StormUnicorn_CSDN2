# 二分逼近求指定数平方根
def sqrt(n):
    low = 0
    high = n
    mid = (low + high) / 2
    precision = 1e-10
    while abs(mid ** 2 - n) > precision:
        if mid ** 2 > n:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
    return mid

#print(sqrt(2))
#print(sqrt(100))

# 牛顿法
def sqrt2(n):
    x = n
    while abs(x ** 2 - n) > 1e-10:
        x = (x + n / x) / 2
    return x

print(sqrt2(2))
