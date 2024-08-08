"""
遍历器for in

# 遍历字符串
for i in 'hello':
    print(i)

# 遍历列表
for i in [1, 2, 3, 4, 5]:
    print(i)

# 乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={:<2}".format(i, j, i*j), end=" ")
    print()
"""

for i in range(6):
    for k in range(5, i, -1):
        print(" ", end=" ")
    for j in range(i*2-1):
        print("*", end=" ")
    print()


