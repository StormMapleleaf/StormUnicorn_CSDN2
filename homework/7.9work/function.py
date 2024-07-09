def funSum(n):
    if n == 1:
        return 1
    else:
        return n + funSum(n-1)


print(funSum(100))