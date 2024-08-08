"""while循环
i = 10
while i >= 1:
   print(i)
    i -= 1   # 换行退缩进退出循环
print("Happy New Year!")

正方形
i = 1
while i <= 9:
    j=1
    while j <= 9:
        print(j, end=" ")
        j += 1
    print()
    i += 1

三角形
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
"""

name = "张三"
age = "20"
str1 = "姓名{0} 年龄{1}".format(name, age)
str2 = "姓名{} 年龄{}".format(name, age)
print(str1)
print(str2)