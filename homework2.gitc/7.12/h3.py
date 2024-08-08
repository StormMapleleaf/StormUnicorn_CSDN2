"""循环逻辑
def fun(n):
    num = 1           # 第n天只剩一个桃子
    while n > 1:
        num = (num + 1) * 2
        n -= 1
    return num
"""



def fun2(n):
    if n == 1:
        return 1
    else:
        return (fun2(n-1) + 1) * 2

print(fun2(3))