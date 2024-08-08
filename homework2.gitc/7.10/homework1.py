# 菱形
def lx(n):
    for i in range(n):
        print(' ' * (n - i) + '*' * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i) + '*' * (2 * i + 1))

lx(5)#参数为半层高

# 空心菱形
def klx(n):
    print(' ' * n + '*')
    for i in range(1, n):
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 1) + '*')
    for i in range(n - 2, 0, -1):
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 1) + '*')
    print(' ' * n + '*')

klx(5)#参数为半层高

# 田字
def tz(n):
    middle = n // 2

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == middle or j == middle:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

tz(7)#参数为长度