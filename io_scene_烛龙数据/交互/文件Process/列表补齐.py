

def 函数(*参数列表): # *args
    列表对象列表 = []
    for o in 参数列表:
        if isinstance(o, list): 列表对象列表.append(o[:])

    列表长度列表 = []
    for o in 列表对象列表: 列表长度列表.append(len(o))

    for o in 列表对象列表:
        for i in range(len(o), max(列表长度列表)): o.append(None)

    return 列表对象列表


# a = [1,2]
# b = []
# c = [3,4,5]
# d = a + c

# o = 函数(a,b,c,d)
# print(o)
# [
#     [1, 2, None, None, None],
#     [None, None, None, None, None],
#     [3, 4, 5, None, None],
#     [1, 2, 3, 4, 5]
#     ]