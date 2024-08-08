# 学生信息管理系统

# 学生信息表
stu = [
    {"name": "张三", "age": 20},
    {"name": "李四", "age": 21},
    {"name": "王五", "age": 22}
]

# 查看功能
def show(s):
    print("| 序号 | 姓名 | 年龄 |")
    for i in range(len(stu)):
        print("|{:^4}".format(i + 1), end=" ")
        print("|{:^4}".format(stu[i]['name']), end="")
        print("|{:^5}".format(stu[i]['age']), end="")
        print("|")

while 1:
    # 菜单
    print(">" * 27)
    print("|", end="")
    print("1:查看", end="|")
    print("2:添加", end="|")
    print("3:删除", end="|")
    print("4:退出", end="|")
    print()
    print(">" * 27)

    # 功能选择
    op = input("请选择功能：")
    if op == "1":
        show(stu)

    elif op == "2":
        stuNew = {}
        stuNew['name'] = input("请输入姓名：")
        stuNew['age'] = input("请输入年龄：")
        stu.append(stuNew)
        input("成功添加，请回车")

    elif op == "3":
        show(stu)
        no = int(input("选择要删除的序号："))
        del stu[no - 1]
        print("删除成功")
        show(stu)
        input("请回车")

    elif op == "4":
        print("退出成功")
        break
    else:
        print("输入错误，请重新输入")