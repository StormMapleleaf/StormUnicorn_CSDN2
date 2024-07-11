# 累加
def funadd(n):
    sum = 0
    sum += n
    if n > 0:
        return sum + funadd(n - 1)
    else:
        return sum

print(funadd(100))

# 递归反转字符串
def funstr(s):
    if s == '':
        return s
    else:
        return funstr(s[1:]) + s[0]

print(funstr('hello'))