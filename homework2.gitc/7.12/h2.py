import random

random_num=random.randint(1,10)
chance = 0
while chance < 3:
    in_num = int(input("请输入一个1-10的数字："))
    if in_num == random_num:
        print("猜对了")
        break
    elif in_num > random_num:
        print("猜大了")
        print("你还有{}次机会".format(2 - chance))
    elif in_num < random_num:
        print("猜小了")
        print("你还有{}次机会".format(2-chance))
    chance += 1

print("结果是{}".format(random_num))


