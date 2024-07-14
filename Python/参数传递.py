# 函数中参数的传递：

# 1普通参数：按照从左到右的方式传递
# def fun1(a,b):
#     print(a,b)

# fun1(10,20)

# # 2默认值参数：从右到左为函数的参数设置默认值
# def fun2(a,b=20,c=10):
#     print(a,b,c)

# fun2("aa")
# fun2("aa","bb")
# fun2(10,20,"dd")

# 3. 关键字参数: 在调用时指定参数名称传递
# def fun3(name,age):
#     print(name,age)

# fun3("aa",20) # 普通参数传递
# fun3(age=20,name="aa") # 在调用时指定参数名称传递（不用考虑参数的传递顺序）

# 4. 非关键字收集参数 *  (收集过来参数是以元组类型呈现)
# def fun4(*params):
#     # print(params) # (10, 20, 30, 40)
#     for i in params:
#         print(i)

# fun4(10,20,30,40)

# 5. 关键字收集参数 **  (收集过来参数是以字段类型呈现)
# def fun5(**params):
#     print(params) # {'age':20, "name":"aa"}

# fun5(age=20,name="aa")

# 6 混合式参数
def demo(*params,m=0):
    print(params)
    print("m:",m)

demo(10,20,50,60,m=300)