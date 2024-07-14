# 汉诺塔程序：

# 声明一个移动函数
# def doMove(n, A, B, C):
#     if n == 1:
#         print(f"将{A}柱上圆盘移至{C}柱")
#     if n == 2:
#         print(f"将{A}柱上圆盘移至{B}柱")
#         print(f"将{A}柱上圆盘移至{C}柱")
#         print(f"将{B}柱上圆盘移至{C}柱")
#     else: # if n == 3:
#         doMove(n-1,A, C, B)
#         print(f"将{A}柱上圆盘移至{C}柱")
#         doMove(n-1,B, A, C)

def doMove(n, A, B, C):
    if n == 1:
        print(f"将{A}柱上第{n}个圆盘移至{C}柱")
    else:
        doMove(n-1,A, C, B)
        print(f"将{A}柱上第{n}个圆盘移至{C}柱")
        doMove(n-1,B, A, C)

#doMove(1, "A", "B", "C")
#doMove(2, "A", "B", "C")
#doMove(3, "A", "B", "C")
doMove(4, "A", "B", "C")

