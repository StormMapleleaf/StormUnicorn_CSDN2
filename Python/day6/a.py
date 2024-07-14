# 练习1： 百元买百鸡（公鸡5元1只，母鸡3元1只，小鸡1元3只）
# 假设：公鸡为x、母鸡y、小鸡z

# 遍历公鸡：
# for x in range(21):
#     # 遍历母鸡:
#     for y in range(34):
#         # 计算小鸡数量
#         z = 100 - x - y
#         # 判断并输出结果(金额100并数量100)
#         if (x*5 + y*3 + z/3) == 100:
#             print(f"公鸡：{x}、 母鸡：{y}、 小鸡：{z}")


# 案例：获取 1~100的所有素数
# 声明一个函数，用于判断当前参数是否是一个素数
# def isM(m):
#     if m <= 1:
#         return False
#     if m <= 3:
#         return True
#     # 遍历 2 ~ m-1 的数值，并使用求余来判断是否不是素数
#     for i in range(2,m // 2 + 1):
#         if m % i == 0:
#             return False  # 不是素数
#     return True

# # 获取 1~100的素数
# for i in range(1,101):
#     if isM(i):
#         print(i)


# 猜数字游戏（三次机会猜 1~10的数值）
import random

target = random.randint(1, 10)
chances = 3 # 初始化一个循环次数

print("欢迎来到猜数字游戏！")
print("你有三次机会猜出 1 到 10 之间的数字。")

# 循环三次
while chances > 0:
    guess = int(input("请输入你的猜测: "))
    if guess == target:
        print("恭喜你，猜对了！")
        break
    elif guess > target:
        print("猜大了，再试试。")
    else:
        print("猜小了，再试试。")
    chances -= 1

# 判断是否循环了3次
if chances == 0:
    print("很遗憾，你的机会用完了。正确数字是", target)
