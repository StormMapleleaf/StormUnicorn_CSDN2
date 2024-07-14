# 变量的作用域：
# 在函数内想修改函数外的全局变量，需要使用global关键字声明一下

# num = 100  #全局变量

# def fun():
#     global num  # 在函数内想修改函数外的全局变量，需要使用global关键字声明一下
#     num += 1
#     print(num)


# fun()
# fun()
# print(num) # 102


# 使用全局变量实现记录函数调用的次数
m = 0
def fun():
    global m
    m += 1
    print(m)

fun()
fun()
fun()
# 全局变量缺乏安全性(会被别人改动的风险)
m =10
fun()
fun()

# （了解）函数可以定义多层嵌套（内部函数）（闭包）
def out():
    mm = 100
    def inner():
        print("aaaaaa", mm)
    return inner # 将内函数返回给调用者

f = out() # 调用外部函数，将内函数返回给变量f
f() # 变量f 加上() 就可以作为函数执行，调用inner内部函数

# inner() # 不可以直接调用内部函数
# print(mm) # 不可调用外函数的局部变量
