

from ... import 数据, 接口


def 函数():
    pass


# def 模型():
#     接口网格_面信息列表 = []
#     for 接口网格 in 数据.变量.选择集.网格列表:
#         面列表 = []
#         for i in range(0, 接口网格.顶点Loop个数, 接口网格.顶点Loop步长): 面列表.append(接口网格.顶点Loop列表[i: i+接口网格.顶点Loop步长])
#         面index列表 = [i for i in range(len(面列表))]
#         接口网格_面信息列表.append([面index列表, 面列表])

#     接口网格_分面列表 = []
#     for 面index列表, 面列表 in 接口网格_面信息列表:
#         分面列表 = []
#         查询面(分面列表, 面index列表, 面列表)
#         接口网格_分面列表.append(分面列表)

#     for 分面列表, [面index列表, 面列表] in zip(接口网格_分面列表, 接口网格_面信息列表):
#         for 区域面index列表 in 分面列表:
#             for 面index in 区域面index列表:
#                 for 顶点index in 面列表[面index]:
#                     pass









def 查询面(分面列表, 范围面index列表, 面列表):
    初始面index列表, 剩余面index列表 = 范围面index列表[0:1], 范围面index列表[1:]
    初始边顶点index列表 = []
    for 面index in 初始面index列表:
        for 顶点index in 面列表[面index]: 初始边顶点index列表.append(顶点index)

    其他面index列表 = []
    结果面index列表 = 初始面index列表[:]
    循环边(初始边顶点index列表, 剩余面index列表, 结果面index列表, 其他面index列表, 面列表)
    if 其他面index列表 == []: 分面列表.append(结果面index列表)
    查询面(其他面index列表, 面列表)


def 循环边(初始边顶点index列表, 范围面index列表, 结果面index列表, 其他面index列表, 面列表):
    剩余面index列表 = []

    循环面index列表 = []
    循环边顶点index列表 = []
    for 面index in 范围面index列表:
        同面布尔 = False
        for 顶点index in 面列表[面index]: # 面顶点列表
            if 顶点index in 初始边顶点index列表: 同面布尔 = True
        if 同面布尔:
            循环面index列表.append(面index)
            for 顶点index in 面列表[面index]: # 面顶点列表
                if 顶点index in 初始边顶点index列表: continue
                循环边顶点index列表.append(顶点index)
        else:
            剩余面index列表.append(面index)

    if 循环边顶点index列表 == []: 其他面index列表 += 范围面index列表
    结果面index列表 += 循环面index列表
    循环边(初始边顶点index列表, 剩余面index列表, 结果面index列表, 面列表)



