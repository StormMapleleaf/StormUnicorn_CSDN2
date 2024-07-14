# 递归程序训练

# 计算指定数值的累加
# def doSum(m):
#     if m == 1:
#         return 1
#     return m + doSum(m-1)

# #测试
# print(doSum(100))

# 获取指定位置的斐波那契数值
def fun(n):
    if n <= 2:  # 若是要前两位上的数值，就返回1
        return 1
    return fun(n-1) + fun(n-2)
# 测试
# print(fun(3)) # 2
print(fun(5)) # 5
print(fun(10)) # 55