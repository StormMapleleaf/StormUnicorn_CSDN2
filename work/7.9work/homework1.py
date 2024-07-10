# 乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={:<2}".format(i, j, i*j), end=" ")
    print()

print()

for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print("{}*{}={:<2}".format(10 - i, j, (10 - i) * j), end=" ")
    print()

print()

for i in range(1, 10):
    for _ in range(1, i):
        print(" " * 6, end=" ")
    for j in range(i, 10):
        print("{}*{}={:<2}".format(i, j, i*j), end=" ")
    print()

print()

for i in range(9, 0, -1):
    for _ in range(9, i, -1):
        print(" " * 6, end=" ")
    for j in range(10 - i, 10):
        print("{}*{}={:<2}".format(10 - i, j, (10 - i) * j), end=" ")
    print()

print()

i = 1
while i < 10:
    j = 1
    while j <= i:
        print("{}*{}={:<2}".format(i, j, i * j), end=" ")
        j += 1
    print()
    i += 1

print()

i = 9
while i > 0:
    j = 1
    while j <= i:
        print("{}*{}={:<2}".format(10 - i, j, (10 - i) * j), end=" ")
        j += 1
    print()
    i -= 1

print()

i = 1
while i < 10:
    # 打印前面的空格
    k = 1
    while k < i:
        print(" " * 6, end=" ")
        k += 1
    # 打印乘法表内容
    j = i
    while j < 10:
        print("{}*{}={:<2}".format(i, j, i * j), end=" ")
        j += 1
    print()
    i += 1

print()

i = 9
while i > 0:
    # 打印前面的空格
    k = 9
    while k > i:
        print(" " * 6, end=" ")
        k -= 1
    # 打印乘法表内容
    j = 10 - i
    while j < 10:
        print("{}*{}={:<2}".format(10 - i, j, (10 - i) * j), end=" ")
        j += 1
    print()
    i -= 1

