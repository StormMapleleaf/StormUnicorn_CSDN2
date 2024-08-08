# 汉诺塔
def hnt(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hnt(n - 1, a, c, b)
        print(a, '-->', c)
        hnt(n - 1, b, a, c)

hnt(3, 'A', 'B', 'C')