def coin_change(coins, amount):
    # 初始化
    total_coin = 0
    # 对可兑换面值列表排序(通过列表的sort函数进行排序，参数reverse为True表示降序排序)
    coins.sort(reverse=True)
    for coin in coins:
       total_coin += amount // coin 
       amount = amount % coin 
       if amount == 0: 
           break
    return total_coin if amount==0 else -1 

# 可兑换面值
coins = [1,10,5,20]
amount = 55 # 总金额
print("兑换零钱数量：",coin_change(coins, amount))