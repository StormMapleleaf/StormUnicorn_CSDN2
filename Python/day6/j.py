# 列表的排序--

a = [12,89,35,67,21,90,8,34]
print("排序前：", a)

# # 循环执行len(a)-1次冒泡
# for j in range(1,len(a)):
#     # 执行一次次冒泡排序（升序）
#     # 遍历列表索引下标
#     for i in range(len(a)-j):
#         # 当前位置上的值与后面的数值做比较
#         if a[i] > a[i+1]:  #若前面大于后面，则执行交换顺序
#             temp = a[i]
#             a[i] = a[i+1]
#             a[i+1] = temp
#     print(f"第{j}冒泡：", a)


# 封装成函数（第一版）
# def mySort(mlist):
#     # 循环冒泡次数
#     for j in range(1,len(mlist)):
#         # 遍历列表索引下标，执行一次次冒泡排序（升序）
#         for i in range(len(mlist)-j):
#             # 当前位置上的值与后面的数值做比较
#             if mlist[i] > mlist[i+1]:  #若前面大于后面，则执行交换顺序
#                 temp = mlist[i]
#                 mlist[i] = mlist[i+1]
#                 mlist[i+1] = temp
#     return mlist

# mySort(a)
# print("排序后：", a)

# 封装成函数（第二版: 带排序规则）
def mySort(mlist, fn):
    # 循环冒泡次数
    for j in range(1,len(mlist)):
        # 遍历列表索引下标，执行一次次冒泡排序（升序）
        for i in range(len(mlist)-j):
            # 当前位置上的值与后面的数值做比较
            if fn(mlist[i], mlist[i+1]):  #若前面大于后面，则执行交换顺序
                temp = mlist[i]
                mlist[i] = mlist[i+1]
                mlist[i+1] = temp
    return mlist


# 定义一个排序规则
# def fun(x,y):
#     return x < y
# # 测试
# mySort(a,fun)
# print(a)


# 测试：对学生信息列表进行年龄的降序排序
stuList = [
    {'name':"zhangsan", 'age':18},
    {'name':"lisi", 'age':21},
    {'name':"wangwu", 'age':19},
    {'name':"zhaoliu", 'age':23},
    {'name':"tianqi", 'age':20},
]

def f(x,y):
    return x['age'] < y['age']

mySort(stuList,f)
print(stuList)

