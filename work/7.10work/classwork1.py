# 1 累加列表中所有元素的和
arr = [[10, 20], [30, 40, 50], [60, 70, 80]]
sum = 0
for i in arr:
    for j in i:
        sum += j
print(sum)

# 2 统计下面列表中每个元素出现的次数,并输出字典
alist = ['aa', 'bb', 'cc', 'bb', 'cc', 'aa', 'cc']
dic = {}
for i in alist:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)

# 3 合并两个列表为字典，定义成函数返回结果
klist = ['sid', 'name', 'price']
vlist = ['1002', '华为手机', '4998']

def hb(klist, vlist):
    dic = {}
    for i in range(len(klist)):
        dic[klist[i]] = vlist[i]
    return dic
print(hb(klist, vlist))

# 4 声明函数mySelect(slist,name)，用于查找列表中的name信息，没有返回None
stuList =[
    {'name': "张三", 'age': "18", 'classid': "python1"},
    {'name': "李四", 'age': "20", 'classid': "python2"}
]

def mySelect(slist, name):
    for i in slist:
        if i['name'] == name:

            return i
    return None
print(mySelect(stuList,'李四'))
