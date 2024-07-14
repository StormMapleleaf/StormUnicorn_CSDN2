# 回调函数： 函数的参数依然是一个函数

def demo(fn):
    fn("Hello") # 蒋参数做一个函数去执行


def fun(info):
    print(info)

#测试
demo(fun)


