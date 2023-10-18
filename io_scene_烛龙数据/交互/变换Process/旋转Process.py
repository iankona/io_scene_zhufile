import os

import bpy
import math
import mathutils
from ... import 数据, 接口, 工具


def rotation_transformation_matrix(coordinate_angle):
    matrix_x = mathutils.Matrix.Rotation(math.radians(coordinate_angle[0]), 4, 'X')
    matrix_y = mathutils.Matrix.Rotation(math.radians(coordinate_angle[1]), 4, 'Y')
    matrix_z = mathutils.Matrix.Rotation(math.radians(coordinate_angle[2]), 4, 'Z')
    return matrix_z @ matrix_y @ matrix_x


def 骨架Process():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        match 数据.变量.旋转.坐标系旋转模式:
            case '自动处理': __armature__xyz__angle__to__auto__coordinate__(插件数据.filepath, 插件数据)
            case '原始数据': pass
            case '手动设置': __armature__xyz__angle__to__sets__coordinate__(插件数据)

def 网格Process():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        match 数据.变量.旋转.坐标系旋转模式:
            case '自动处理': __mesh__xyz__angle__to__auto__coordinate__(插件数据.filepath, 插件数据)
            case '原始数据': pass
            case '手动设置': __mesh__xyz__angle__to__sets__coordinate__(插件数据)



def __armature__xyz__angle__to__auto__coordinate__(filepath, 插件数据):
    match os.path.splitext(filepath)[-1]:
        case ".fbx"  : __骨架__手动处理__骨骼旋转变换__([  0, 90, 0], 插件数据.文件骨架)
        case ".nif"  : pass # 无需旋转
        case ".xac"  : __骨架__手动处理__骨骼旋转变换__([180, 90, 0], 插件数据.文件骨架)
        case ".vmesh": pass # 无需旋转
        case ".model": pass # 无需旋转
        case ".srt"  : pass # 无需旋转

def __mesh__xyz__angle__to__auto__coordinate__(filepath, 插件数据):
    match os.path.splitext(filepath)[-1]:
        case ".fbx"  : __网格__手动处理__位置旋转变换__([  0, 90, 0], 插件数据)
        case ".nif"  : pass # 无需旋转
        case ".xac"  : __网格__手动处理__位置旋转变换__([180, 90, 0], 插件数据)
        case ".vmesh": pass # 无需旋转
        case ".model": pass # 无需旋转
        case ".srt"  : pass # 无需旋转


def __armature__xyz__angle__to__sets__coordinate__(插件数据):
    x_angle, y_angle, z_angle = int(数据.变量.旋转.绕X轴旋转[0:-1]), int(数据.变量.旋转.绕Y轴旋转[0:-1]), int(数据.变量.旋转.绕Z轴旋转[0:-1])
    __骨架__手动处理__骨骼旋转变换__([x_angle, y_angle, z_angle], 插件数据.文件骨架)

def __mesh__xyz__angle__to__sets__coordinate__(插件数据):
    x_angle, y_angle, z_angle = int(数据.变量.旋转.绕X轴旋转[0:-1]), int(数据.变量.旋转.绕Y轴旋转[0:-1]), int(数据.变量.旋转.绕Z轴旋转[0:-1])
    __网格__手动处理__位置旋转变换__([x_angle, y_angle, z_angle], 插件数据)




def __骨架__手动处理__骨骼旋转变换__(coordinate_angle, 文件骨架):
    # 骨架的旋转，不会影响姿态导入，姿态无需跟着一起旋转。神奇的矩阵！
    if 文件骨架 == None: return None
    angle_matrix = rotation_transformation_matrix(coordinate_angle)
    for 骨骼名称, 文件骨骼 in 文件骨架.骨骼字典.items():
        # 等价于 文件骨骼.matrix_local = angle_matrix @ 文件骨骼.matrix_local
        文件骨骼.location = angle_matrix @ 文件骨骼.location
        文件骨骼.rotation_quaternion = (angle_matrix @ 文件骨骼.rotation_quaternion.to_matrix().to_4x4()).to_quaternion()
        # 文件骨骼.matrix_local = mathutils.Matrix.LocRotScale(文件骨骼.location, 文件骨骼.rotation_quaternion, 文件骨骼.scale)
        # 文件骨骼.matrix_local = angle_matrix @ 文件骨骼.matrix_local
        # location, rotation_quaternion, scale = 文件骨骼.matrix_local.decompose()
        # 文件骨骼.location = location
        # 文件骨骼.rotation_quaternion = rotation_quaternion
        # 文件骨骼.scale = scale



def __网格__手动处理__位置旋转变换__(coordinate_angle, 插件数据):
    angle_matrix = rotation_transformation_matrix(coordinate_angle)
    for 插件网格 in 插件数据.插件网格列表:
        for i, 顶点位置 in enumerate(插件网格.顶点列表): 
            插件网格.顶点列表[i] = angle_matrix @ 顶点位置

        for 形态名称, slidermin, slidermax, 形态键 in 插件网格.形态键列表:
            for i, 顶点位置 in enumerate(形态键): 形态键[i] = angle_matrix @ 顶点位置

