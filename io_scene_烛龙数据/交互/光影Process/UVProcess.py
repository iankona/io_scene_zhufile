import os


from ... import 数据




def UV处理():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for 插件网格 in 插件数据.插件网格列表:
            match 数据.变量.UV.处理模式:
                case "自动处理": 自动处理(插件数据.filepath, 插件网格)
                case "原始数据": return
                case "手动设置": 手动处理(插件网格)



def 自动处理(filepath, 插件网格):
    match os.path.splitext(filepath)[-1]:
        case ".nif":
            镜像V轴(插件网格)
        case ".xac":
            镜像V轴(插件网格)
            U轴负域镜像正域(插件网格)
        case ".vmesh":
            镜像V轴(插件网格)
        case ".model":
            镜像V轴(插件网格)
        case ".srt":
            镜像V轴(插件网格)

def 手动处理(插件网格):
    if 数据.变量.UV.U轴翻转: U轴翻转(插件网格)
    if 数据.变量.UV.V轴翻转: V轴翻转(插件网格)
    X距离 = float(数据.变量.UV.U轴移动)
    Y距离 = float(数据.变量.UV.V轴移动)
    U轴移动(插件网格, X距离), V轴移动(插件网格, Y距离)
    if 数据.变量.UV.U轴负域镜像正域: U轴负域镜像正域(插件网格)
    if 数据.变量.UV.V轴负域镜像正域: V轴负域镜像正域(插件网格)


def 镜像U轴(插件网格):
    for i, [u, v] in enumerate(插件网格.顶点UV列表): # 等价1-u
        u = -u
        u = u + 1
        插件网格.顶点UV列表[i] = [u, v]


def 镜像V轴(插件网格):
    for i, [u, v] in enumerate(插件网格.顶点UV列表):
        v = -v
        v = v + 1
        插件网格.顶点UV列表[i] = [u, v]


def U轴翻转(插件网格):
    for i, [u, v] in enumerate(插件网格.顶点UV列表):
        u = -u
        插件网格.顶点UV列表[i] = [u, v]

def V轴翻转(插件网格):
    for i, [u, v] in enumerate(插件网格.顶点UV列表):
        v = -v
        插件网格.顶点UV列表[i] = [u, v]


def U轴移动(插件网格, num):
    for i, [u, v] in enumerate(插件网格.顶点UV列表):
        u = u + num
        插件网格.顶点UV列表[i] = [u, v]


def V轴移动(插件网格, num):
    for i, [u, v] in enumerate(插件网格.顶点UV列表):
        v = v + num
        插件网格.顶点UV列表[i] = [u, v]


def U轴负域镜像正域(插件网格):
    for i, [u, v] in enumerate(插件网格.顶点UV列表):
        if u < 0: u = -u
        插件网格.顶点UV列表[i] = [u, v]


def V轴负域镜像正域(插件网格):
    for i, [u, v] in enumerate(插件网格.顶点UV列表):
        if v < 0: v = -v
        插件网格.顶点UV列表[i] = [u, v]

