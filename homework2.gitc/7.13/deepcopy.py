def mydeepcopy(obj):
    if isinstance(obj, dict):
        return {mydeepcopy(key): mydeepcopy(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [mydeepcopy(element) for element in obj]
    elif isinstance(obj, set):
        return {mydeepcopy(element) for element in obj}
    else:
        return obj

# 测试 mydeepcopy 函数
olist = [1, [2, 3], 4,5]
clist = mydeepcopy(olist)

odict = {'x': 1, 'y': [2, 3]}
cdict = mydeepcopy(odict)

oset = {1, 2, (3, 4)}
cset = mydeepcopy(oset)

print('list:', olist)
print('clist:', clist)
print()
print('dict:', odict)
print('cdict:', cdict)
print()
print('set:', oset)
print('cset:', cset)




