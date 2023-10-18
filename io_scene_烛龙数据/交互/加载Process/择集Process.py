import os
import bpy
import math
import mathutils
from ... import 数据, 接口


from . import data_to_collection
from . import data_to_armatureobj


def 新建collection():
    if 数据.变量.选择集.名称 == "": # or 数据.变量.选择集.名称 == "Collection": # 文件姿态会挂载到这个选择集上面，从而不用新建选择集
        数据.变量.选择集.软件collection = bpy.context.scene.collection
        return None
    
    if 数据.变量.选择.导入模式 == '引用现有选择集' and 数据.变量.选择集.名称 in bpy.data.collections:
        数据.变量.选择集.软件collection = bpy.data.collections[数据.变量.选择集.名称]
    else:
        数据.变量.选择集.软件collection = data_to_collection.新建选择集(数据.变量.选择集.名称)

def move_objects_from_collection_to_collection():
    # 从 bpy.context.scene.collection 中移动 object
    if 数据.变量.选择集.软件armatureobj != None: # 若为 None，Blender会直接崩溃跳出
        bpy.context.scene.collection.objects.unlink(数据.变量.选择集.软件armatureobj)
        数据.变量.选择集.软件collection.objects.link(数据.变量.选择集.软件armatureobj)

    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.软件armatureobj != None: # 若为 None，Blender会直接崩溃跳出
            bpy.context.scene.collection.objects.unlink(插件数据.软件armatureobj)
            数据.变量.选择集.软件collection.objects.link(插件数据.软件armatureobj)
        for object in 插件数据.软件objects:
            bpy.context.scene.collection.objects.unlink(object)
            数据.变量.选择集.软件collection.objects.link(object)



def 合并与略过骨架():
    match 数据.变量.骨架.骨架导入模式:
        case "合并骨架": __合并骨架__()
        case "各自骨架": pass
        case "略过骨架": __略过骨架__()


def __合并骨架__():
    骨骼字典 = {}
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.插件骨架 == None: continue
        for 骨骼名称, 插件骨骼 in 插件数据.插件骨架.骨骼字典.items():  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
            骨骼字典[骨骼名称] = 插件骨骼

    if 骨骼字典 == {}: return None # 只处理了只有动画文件，没有其他文件的情况
    数据.变量.选择集.插件骨架 = 接口.结构.插件骨架() 
    数据.变量.选择集.插件骨架.骨骼字典 = 骨骼字典
    数据.变量.选择集.armaturepath = 数据.变量.选择集.插件数据列表[0].filepath
    for 插件数据 in 数据.变量.选择集.插件数据列表: 插件数据.插件骨架 = None


def __略过骨架__():
    数据.变量.选择集.插件骨架 = None
    for 插件数据 in 数据.变量.选择集.插件数据列表: 插件数据.插件骨架 = None


def 左右手指长度一致():
    列表1 = ['Bip01 L Hand', 
             'Bip01 L Finger0','Bip01 L Finger01','Bip01 L Finger02','Bip01 L Finger0Nub',
             'Bip01 L Finger1','Bip01 L Finger11','Bip01 L Finger12','Bip01 L Finger1Nub',
             'Bip01 L Finger2','Bip01 L Finger21','Bip01 L Finger22','Bip01 L Finger2Nub',
             'Bip01 L Finger3','Bip01 L Finger31','Bip01 L Finger32','Bip01 L Finger3Nub',
             'Bip01 L Finger4','Bip01 L Finger41','Bip01 L Finger42','Bip01 L Finger4Nub',
             ]
    列表2 = ['Bip01 R Hand', 
             'Bip01 R Finger0','Bip01 R Finger01','Bip01 R Finger02','Bip01 R Finger0Nub',
             'Bip01 R Finger1','Bip01 R Finger11','Bip01 R Finger12','Bip01 R Finger1Nub',
             'Bip01 R Finger2','Bip01 R Finger21','Bip01 R Finger22','Bip01 R Finger2Nub',
             'Bip01 R Finger3','Bip01 R Finger31','Bip01 R Finger32','Bip01 R Finger3Nub',
             'Bip01 R Finger4','Bip01 R Finger41','Bip01 R Finger42','Bip01 R Finger4Nub',
             ]

    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.插件骨架 == None: continue
        for lname, rname in zip(列表1, 列表2): __手指长度一致__(lname, rname, 插件数据.插件骨架)
    if 数据.变量.选择集.插件骨架 != None: 
        for lname, rname in zip(列表1, 列表2): __手指长度一致__(lname, rname, 数据.变量.选择集.插件骨架)

def __手指长度一致__(lname, rname, 插件骨架):
    if lname in 插件骨架.骨骼字典 and rname in 插件骨架.骨骼字典:
        l_length = 插件骨架.骨骼字典[lname].length
        r_length = 插件骨架.骨骼字典[rname].length
        length = min(l_length, r_length)
        插件骨架.骨骼字典[lname].length = length
        插件骨架.骨骼字典[rname].length = length




def 新建armatureobj():
    if 数据.变量.选择集.插件骨架 == None: return None
    数据.变量.选择集.软件armatureobj = data_to_armatureobj.新建骨架对象(数据.变量.选择集.名称, 数据.变量.选择集.插件骨架)



def 古剑1新建Break子选择集and移动Objects():
    breakobjects = []
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for object in 插件数据.软件objects:
            if "_break" in object.name: breakobjects.append(object)

    if breakobjects == []: return None

    # 从 collection 中移动 object
    if 数据.变量.选择集.软件collection == bpy.context.scene.collection:
        filepath = 数据.变量.选择集.插件数据列表[0].filepath
        collection_name = os.path.split(filepath)[-1]
        数据.变量.选择集.软件collection = data_to_collection.新建选择集(collection_name)

        for 插件数据 in 数据.变量.选择集.插件数据列表:
            if 插件数据.软件armatureobj != None:
                bpy.context.scene.collection.objects.unlink(插件数据.软件armatureobj)
                数据.变量.选择集.软件collection.objects.link(插件数据.软件armatureobj)
            for object in 插件数据.软件objects:
                bpy.context.scene.collection.objects.unlink(object)
                数据.变量.选择集.软件collection.objects.link(object)


    breakcollection = bpy.data.collections.new(数据.变量.选择集.软件collection.name + "_break")
    数据.变量.选择集.软件collection.children.link(breakcollection)

    for object in breakobjects:
        object.parent = None
        object.modifiers.clear()
        数据.变量.选择集.软件collection.objects.unlink(object)
        breakcollection.objects.link(object)



def 合并文件姿态():
    match 数据.变量.姿态.动画合并模式:
        case '原始数据': pass
        case '姿态相加': __合并动画__姿态相加__()
        case '姿态顾前': __合并动画__姿态顾前__()
        case '姿态顾后': __合并动画__姿态顾后__()



def __合并动画__姿态相加__():
    数据.变量.选择集.文件姿态 = 接口.结构.文件姿态()
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.文件姿态 == None: continue
        for 骨骼名称, 姿态骨骼 in 插件数据.文件姿态.骨骼字典.items():
            if 骨骼名称 not in 数据.变量.选择集.文件姿态.骨骼字典:
                数据.变量.选择集.文件姿态.骨骼字典[骨骼名称] = 姿态骨骼
            else:
                选择骨骼 = 数据.变量.选择集.文件姿态.骨骼字典[骨骼名称]
                文件骨骼 = 插件数据.文件姿态.骨骼字典[骨骼名称]
                __文件骨骼__姿态相加__(选择骨骼, 文件骨骼)

    for 插件数据 in 数据.变量.选择集.插件数据列表:
        插件数据.文件姿态 = None
        数据.变量.选择集.actionpath = 插件数据.filepath

def __合并动画__姿态顾前__():
    数据.变量.选择集.文件姿态 = 接口.结构.文件姿态()
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.文件姿态 == None: continue
        for 骨骼名称, 姿态骨骼 in 插件数据.文件姿态.骨骼字典.items():
            if 骨骼名称 not in 数据.变量.选择集.文件姿态.骨骼字典:
                数据.变量.选择集.文件姿态.骨骼字典[骨骼名称] = 姿态骨骼
            else:
                选择骨骼 = 数据.变量.选择集.文件姿态.骨骼字典[骨骼名称]
                文件骨骼 = 插件数据.文件姿态.骨骼字典[骨骼名称]
                __文件骨骼__姿态顾前__(选择骨骼, 文件骨骼)

    for 插件数据 in 数据.变量.选择集.插件数据列表:
        插件数据.文件姿态 = None
        数据.变量.选择集.actionpath = 插件数据.filepath


def __合并动画__姿态顾后__():
    数据.变量.选择集.文件姿态 = 接口.结构.文件姿态()
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.文件姿态 == None: continue
        for 骨骼名称, 姿态骨骼 in 插件数据.文件姿态.骨骼字典.items():
            if 骨骼名称 not in 数据.变量.选择集.文件姿态.骨骼字典:
                数据.变量.选择集.文件姿态.骨骼字典[骨骼名称] = 姿态骨骼
            else:
                选择骨骼 = 数据.变量.选择集.文件姿态.骨骼字典[骨骼名称]
                文件骨骼 = 插件数据.文件姿态.骨骼字典[骨骼名称]
                __文件骨骼__姿态顾后__(选择骨骼, 文件骨骼)

    for 插件数据 in 数据.变量.选择集.插件数据列表: 
        插件数据.文件姿态 = None
        数据.变量.选择集.actionpath = 插件数据.filepath


def __文件骨骼__姿态相加__(选择骨骼, 文件骨骼):
    位置帧字典 = {}
    for frame, location in 选择骨骼.位置帧列表: 位置帧字典[round(frame)] = location
    for frame, location in 文件骨骼.位置帧列表:
        time = round(frame)
        if time not in 位置帧字典: 
            位置帧字典[time] = location
        else:
            位置帧字典[time] = 位置帧字典[time] + location

    旋转帧字典 = {}
    for frame, rotation in 选择骨骼.旋转帧列表: 旋转帧字典[round(frame)] = rotation
    for frame, rotation in 文件骨骼.旋转帧列表:
        time = round(frame)
        if time not in 旋转帧字典: 
            旋转帧字典[time] = rotation
        else:
            旋转帧字典[time] = rotation @ 旋转帧字典[time]

    缩放帧字典 = {}
    for frame, scale in 选择骨骼.缩放帧列表: 缩放帧字典[round(frame)] = scale
    for frame, scale in 文件骨骼.缩放帧列表:
        time = round(frame)
        if time not in 缩放帧字典: 
            缩放帧字典[time] = scale
        else:
            缩放帧字典[time] = 缩放帧字典[time] + scale

    frame_sort_list = sorted(位置帧字典.keys())
    位置帧列表 = []
    for frame in frame_sort_list: 位置帧列表.append([frame, 位置帧字典[frame]])

    frame_sort_list = sorted(旋转帧字典.keys())
    旋转帧列表 = []
    for frame in frame_sort_list: 旋转帧列表.append([frame, 旋转帧字典[frame]])

    frame_sort_list = sorted(缩放帧字典.keys())
    缩放帧列表 = []
    for frame in frame_sort_list: 缩放帧列表.append([frame, 缩放帧字典[frame]])

    选择骨骼.位置帧列表 = 位置帧列表
    选择骨骼.旋转帧列表 = 旋转帧列表
    选择骨骼.缩放帧列表 = 缩放帧列表


def __文件骨骼__姿态顾前__(选择骨骼, 文件骨骼):
    位置帧字典 = {}
    for frame, location in 选择骨骼.位置帧列表: 位置帧字典[round(frame)] = location
    for frame, location in 文件骨骼.位置帧列表:
        time = round(frame)
        if time not in 位置帧字典: 位置帧字典[time] = location

    旋转帧字典 = {}
    for frame, rotation in 选择骨骼.旋转帧列表: 旋转帧字典[round(frame)] = rotation
    for frame, rotation in 文件骨骼.旋转帧列表:
        time = round(frame)
        if time not in 旋转帧字典: 旋转帧字典[time] = rotation

    缩放帧字典 = {}
    for frame, scale in 选择骨骼.缩放帧列表: 缩放帧字典[round(frame)] = scale
    for frame, scale in 文件骨骼.缩放帧列表:
        time = round(frame)
        if time not in 缩放帧字典: 缩放帧字典[time] = scale

    frame_sort_list = sorted(位置帧字典.keys())
    位置帧列表 = []
    for frame in frame_sort_list: 位置帧列表.append([frame, 位置帧字典[frame]])

    frame_sort_list = sorted(旋转帧字典.keys())
    旋转帧列表 = []
    for frame in frame_sort_list: 旋转帧列表.append([frame, 旋转帧字典[frame]])

    frame_sort_list = sorted(缩放帧字典.keys())
    缩放帧列表 = []
    for frame in frame_sort_list: 缩放帧列表.append([frame, 缩放帧字典[frame]])

    选择骨骼.位置帧列表 = 位置帧列表
    选择骨骼.旋转帧列表 = 旋转帧列表
    选择骨骼.缩放帧列表 = 缩放帧列表


def __文件骨骼__姿态顾后__(选择骨骼, 文件骨骼):
    位置帧字典 = {}
    for frame, location in 选择骨骼.位置帧列表: 位置帧字典[round(frame)] = location
    for frame, location in 文件骨骼.位置帧列表: 位置帧字典[round(frame)] = location

    旋转帧字典 = {}
    for frame, rotation in 选择骨骼.旋转帧列表: 旋转帧字典[round(frame)] = rotation
    for frame, rotation in 文件骨骼.旋转帧列表: 旋转帧字典[round(frame)] = rotation

    缩放帧字典 = {}
    for frame, scale in 选择骨骼.缩放帧列表: 缩放帧字典[round(frame)] = scale
    for frame, scale in 文件骨骼.缩放帧列表: 缩放帧字典[round(frame)] = scale

    frame_sort_list = sorted(位置帧字典.keys())
    位置帧列表 = []
    for frame in frame_sort_list: 位置帧列表.append([frame, 位置帧字典[frame]])

    frame_sort_list = sorted(旋转帧字典.keys())
    旋转帧列表 = []
    for frame in frame_sort_list: 旋转帧列表.append([frame, 旋转帧字典[frame]])

    frame_sort_list = sorted(缩放帧字典.keys())
    缩放帧列表 = []
    for frame in frame_sort_list: 缩放帧列表.append([frame, 缩放帧字典[frame]])

    选择骨骼.位置帧列表 = 位置帧列表
    选择骨骼.旋转帧列表 = 旋转帧列表
    选择骨骼.缩放帧列表 = 缩放帧列表



def 文件骨架新建T姿势action():
    if 数据.变量.骨架.启用导入骨架添加T姿势 == False: return None
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.软件armatureobj == None: continue
        __设置T姿势__(插件数据.filepath, 插件数据.软件armatureobj)
    if 数据.变量.选择集.软件armatureobj != None:
        __设置T姿势__(数据.变量.选择集.armaturepath, 数据.变量.选择集.软件armatureobj)


def __设置T姿势__(filepath, 软件armatureobj):
    match os.path.splitext(filepath)[-1]:
        case ".nif"  : __古剑3__设置T姿势__(软件armatureobj)
        case ".xac"  : __古剑2__设置T姿势__(软件armatureobj)
        case ".model": __古剑3__设置T姿势__(软件armatureobj)

   
def __古剑2__设置T姿势__(软件armatureobj):
    软件armatureobj.animation_data_create()
    软件armatureobj.animation_data.action = bpy.data.actions.new(软件armatureobj.name+"_T_pose")
    for pbone in 软件armatureobj.pose.bones:
        for chars in ["UpperArm", "UpArmTwist"]:
            if chars in pbone.name and 数据.变量.骨架.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                euler = mathutils.Euler([0, 0, -z_rad], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)

        for chars in ["ForeTwist", "Forearm", "Finger01", "Finger02", "Finger01Nub", "Finger1", "Finger2", "Finger3", "Finger4"]:
            if chars in pbone.name and 数据.变量.骨架.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                # print(pbone.name, x_angle, y_angle, z_angle) # print(math.radians(90)) # 1.5707963267948966
                euler = mathutils.Euler([-x_rad, 0, 0], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)


        for chars in ["Hand"]:
            if chars in pbone.name and 数据.变量.骨架.Hand展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([0, vy, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)


        if pbone.name == "Bip01 R Finger0" or pbone.name == "Bip01 L Finger0":
            if 数据.变量.骨架.Finger0展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, vy, 0]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)


        for chars in ["Clavicle"]:  
            if chars in pbone.name and 数据.变量.骨架.Clavicle展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, 0, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)



def __古剑3__设置T姿势__(软件armatureobj):
    软件armatureobj.animation_data_create()
    软件armatureobj.animation_data.action = bpy.data.actions.new(软件armatureobj.name+"_T_pose")
    for pbone in 软件armatureobj.pose.bones:
        for chars in ["UpperArm", "uparm"]:
            if chars in pbone.name and 数据.变量.骨架.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                # print(pbone.name, x_angle, y_angle, z_angle) # print(math.radians(90)) # 1.5707963267948966
                euler = mathutils.Euler([-x_rad, 0, 0], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)

        for chars in ["ForeTwist", "Forearm", "Finger01", "Finger02", "Finger01Nub", "Finger1", "Finger2", "Finger3", "Finger4"]:
            if chars in pbone.name and 数据.变量.骨架.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                # print(pbone.name, x_angle, y_angle, z_angle) # print(math.radians(90)) # 1.5707963267948966
                euler = mathutils.Euler([0, 0, -z_rad], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)


        for chars in ["Hand"]:
            if chars in pbone.name and 数据.变量.骨架.Hand展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, vy, 0]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)


        if pbone.name == "Bip01 R Finger0" or pbone.name == "Bip01 L Finger0":
            if 数据.变量.骨架.Finger0展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([0, vy, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)


        for chars in ["Clavicle"]:
            if chars in pbone.name and 数据.变量.骨架.Clavicle展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, 0, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=0)