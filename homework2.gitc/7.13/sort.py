#自定义冒泡排序
def myBubble(mylist, fn):
    for j in range(1,len(mylist)):
        for i in range(len(mylist)-j):
            if fn(mylist[i], mylist[i+1]):
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
    return mylist


sList = [
    {'name':"zhangsan", 'age':18},
    {'name':"lisi", 'age':11},
    {'name':"wangwu", 'age':19},
    {'name':"zhaoliu", 'age':23},
    {'name':"tianqi", 'age':28},
]

def up(x,y):
    return x['age'] > y['age']

myBubble(sList,up)
print(sList)


