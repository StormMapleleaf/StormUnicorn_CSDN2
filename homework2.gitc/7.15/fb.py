def fibonacci(n):
    a, b = 1, 1
    mlist = [1,1]
    for i in range(n-2):
        a, b = b, a + b
        mlist.append(b)
    return mlist

print(fibonacci(4))