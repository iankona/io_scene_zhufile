import os
import mathutils

from . import loc_basis_coordinate_process
from . import bone_space_2_basis_space, basis_space_2_basis_space
from ... import 数据, 接口


# 准备数据 -> 空间变换 -> 通道各自变换

def 预处理姿态():
    __预处理姿态_选择骨架__()
    __预处理姿态_姿态骨架__()



def __预处理姿态_选择骨架__():
    数据.变量.选择骨架and插件姿态列表 = []
    for 软件armatureobj in 数据.变量.选择骨架列表:
        插件姿态列表 = []
        for 插件数据 in 数据.变量.选择集.插件数据列表:
            if 插件数据.文件姿态 == None: continue
            插件姿态 = __文件姿态__to__插件姿态__(插件数据.文件姿态)
            插件姿态列表.append([插件数据.filepath, 插件数据.文件姿态, 插件姿态])
        if 数据.变量.选择集.文件姿态 != None:
            插件姿态 = __文件姿态__to__插件姿态__(数据.变量.选择集.文件姿态)
            插件姿态列表.append([数据.变量.选择集.actionpath, 数据.变量.选择集.文件姿态, 插件姿态])
        数据.变量.选择骨架and插件姿态列表.append( [软件armatureobj, 插件姿态列表] )


def __预处理姿态_姿态骨架__():
    数据.变量.姿态骨架and插件姿态列表 = []
    for 软件armatureobj in 数据.变量.姿态骨架列表:
        插件姿态列表 = []
        for 插件数据 in 数据.变量.选择集.插件数据列表:
            if 插件数据.文件姿态 == None: continue
            if 插件数据.软件armatureobj != 软件armatureobj: continue
            插件姿态 = __文件姿态__to__插件姿态__(插件数据.文件姿态)
            插件姿态列表.append([插件数据.filepath, 插件数据.文件姿态, 插件姿态])
            break
        数据.变量.姿态骨架and插件姿态列表.append( [软件armatureobj, 插件姿态列表] )



def __文件姿态__to__插件姿态__(文件姿态):
    插件姿态 = 接口.结构.插件姿态()
    for 骨骼名称, 文件骨骼 in 文件姿态.骨骼字典.items():
        插件骨骼 = 插件姿态.骨骼()
        插件骨骼.名称 = 骨骼名称
        插件姿态.骨骼字典[骨骼名称] = 插件骨骼
    return 插件姿态



def Auto姿态_to_Basis姿态():
    __Auto姿态__to__Basis姿态__选择骨架__()
    __Auto姿态__to__Basis姿态__姿态骨架__()


def __Auto姿态__to__Basis姿态__选择骨架__():
    if 数据.变量.选择骨架and插件姿态列表 == []: return None
    for 软件armatureobj, 插件姿态列表 in 数据.变量.选择骨架and插件姿态列表:
        for filepath, 文件姿态, 插件姿态 in 插件姿态列表: 
            __位置通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态)
            __旋转通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态)
            __缩放通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态)


def __Auto姿态__to__Basis姿态__姿态骨架__():
    if 数据.变量.姿态骨架and插件姿态列表 == []: return None
    for 软件armatureobj, 插件姿态列表 in 数据.变量.姿态骨架and插件姿态列表:
        for filepath, 文件姿态, 插件姿态 in 插件姿态列表: 
            __位置通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态)
            __旋转通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态)
            __缩放通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态)



def __位置通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态):
    match 数据.变量.姿态通道位置.位置导入空间:
        case 'Auto_Space' : __location__auto__spcae__to__basis__space__(软件armatureobj, filepath, 文件姿态, 插件姿态)
        case 'Bone_Space' : bone_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)
        case 'Basis_Space': basis_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)

def __旋转通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态): 
    match 数据.变量.姿态通道旋转.旋转导入空间:
        case 'Auto_Space' : __rotation__auto__spcae__to__basis__space__(软件armatureobj, filepath, 文件姿态, 插件姿态)
        case 'Bone_Space' : bone_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)
        case 'Basis_Space': basis_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)

def __缩放通道__Auto空间__to__Basis空间__(软件armatureobj, filepath, 文件姿态, 插件姿态):
    match 数据.变量.姿态通道缩放.缩放导入空间:
        case 'Auto_Space' : __scale__auto__spcae__to__basis__space__(软件armatureobj, filepath, 文件姿态, 插件姿态)
        case 'Bone_Space' : bone_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)
        case 'Basis_Space': basis_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)


def __location__auto__spcae__to__basis__space__(软件armatureobj, filepath, 文件姿态, 插件姿态):
    match os.path.splitext(filepath)[-1]:
        case ".fbx": bone_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)
        case ".kf" : bone_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)
        case ".xsm": bone_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)
        case ".hka": basis_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)
        case ".hkx": bone_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)
        case   _   : bone_space_2_basis_space.location(软件armatureobj, 文件姿态, 插件姿态)

def __rotation__auto__spcae__to__basis__space__(软件armatureobj, filepath, 文件姿态, 插件姿态):
    match os.path.splitext(filepath)[-1]:
        case ".fbx": bone_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)
        case ".kf" : bone_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)
        case ".xsm": bone_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)
        case ".hka": bone_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)
        case ".hkx": bone_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)
        case   _   : bone_space_2_basis_space.rotation_quaternion(软件armatureobj, 文件姿态, 插件姿态)



def __scale__auto__spcae__to__basis__space__(软件armatureobj, filepath, 文件姿态, 插件姿态):
    match os.path.splitext(filepath)[-1]:
        case ".fbx": bone_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)
        case ".kf" : bone_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)
        case ".xsm": bone_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)
        case ".hka": bone_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)
        case ".hkx": bone_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)
        case   _   : bone_space_2_basis_space.scale(软件armatureobj, 文件姿态, 插件姿态)




