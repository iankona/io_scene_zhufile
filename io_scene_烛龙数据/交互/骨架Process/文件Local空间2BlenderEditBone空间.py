import os

import bpy
from ... import 数据, 接口
from . import armature_bone_coordinate_process


def 文件骨架_Matrix_Local_Decompose():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.文件骨架 == None: continue
        __文件骨骼__Matrix__Local__Decompose__(插件数据.文件骨架)


def __文件骨骼__Matrix__Local__Decompose__(文件骨架):
    for 骨骼名称, 文件骨骼 in 文件骨架.骨骼字典.items():
        location, rotation_quaternion, scale = 文件骨骼.matrix_local.decompose()
        文件骨骼.location = location
        文件骨骼.rotation_quaternion = rotation_quaternion
        文件骨骼.scale = scale




def 插件数据_转换处理():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.文件骨架 == None: continue
        插件数据.插件骨架 = __骨架转换__Local空间__to__EditBone空间__(插件数据.文件骨架)


def __骨架转换__Local空间__to__EditBone空间__(文件骨架):
    插件骨架 = 接口.结构.插件骨架()
    for 骨骼名称, 文件骨骼 in 文件骨架.骨骼字典.items():
        插件骨骼 = 插件骨架.骨骼()
        插件骨骼.name = 文件骨骼.name
        插件骨骼.head = 文件骨骼.location
        direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(文件骨骼.rotation_quaternion.to_matrix())
        插件骨骼.tail = 文件骨骼.location + direct_local
        插件骨骼.roll = roll_local
        插件骨架.骨骼字典[骨骼名称] = 插件骨骼

        if 文件骨骼.parentname == "": continue
        插件骨骼.parent = 插件骨架.骨骼字典[文件骨骼.parentname]
    return 插件骨架


