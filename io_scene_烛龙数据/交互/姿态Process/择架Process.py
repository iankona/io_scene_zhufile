import bpy
import traceback
from ... import 数据


def find_blender_armatures():
    # 处理blender中选中的骨架
    数据.变量.选择骨架列表 = []
    match 数据.变量.姿态.骨架选择模式:
        case '当前选中(多选)': __当前多选__()
        case 'armatures[:]': __全选对象__()
        case 'armatures[0]': __选择前端__()
        case 'armatures[-1]': __选择尾端__()

    # 处理文件浏览器，同时选择模型和动画的情况
    __同选姿态自动添加到同选择模型__()

    # 处理模型中，既有骨架，又有动画的情况
    数据.变量.姿态骨架列表 = []
    __同选姿态自动添加到同文件骨架__()


def __当前多选__():
    for object in bpy.context.selected_objects:
        if object.type != "ARMATURE": continue
        if object not in 数据.变量.选择骨架列表: 数据.变量.选择骨架列表.append(object)


def __全选对象__():
    for object in bpy.data.objects:
        if object.type != "ARMATURE": continue
        if object not in 数据.变量.选择骨架列表: 数据.变量.选择骨架列表.append(object)


def __选择前端__():
    for object in bpy.data.objects:
        if object.type == "ARMATURE": 
            if object not in 数据.变量.选择骨架列表: 
                数据.变量.选择骨架列表.append(object)
                break


def __选择尾端__():
    for object in bpy.data.objects[::-1]:
        if object.type == "ARMATURE": 
            if object not in 数据.变量.选择骨架列表: 
                数据.变量.选择骨架列表.append(object)
                break


def __同选姿态自动添加到同选择模型__():
    存在骨架, 存在姿态 = False, False
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.文件姿态 != None: 存在姿态 = True
        if 插件数据.软件armatureobj != None: 存在骨架 = True
    if 存在骨架 and 存在姿态:
        for 插件数据 in 数据.变量.选择集.插件数据列表:
            if 插件数据.软件armatureobj == None: continue
            数据.变量.选择骨架列表.append(插件数据.软件armatureobj)


def __同选姿态自动添加到同文件骨架__():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.文件姿态 == None: continue
        if 插件数据.软件armatureobj == None: continue
        if 插件数据.软件armatureobj in 数据.变量.姿态骨架列表: continue
        数据.变量.姿态骨架列表.append(插件数据.软件armatureobj)

# MESH
# ARMATURE