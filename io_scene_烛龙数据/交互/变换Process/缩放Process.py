import os
import math
import mathutils
from ... import 数据, 接口, 工具


def scale_transformation_matrix(view_direction=["-Y", "X", "Z"]):
    matrix = [ [1.0, 0.0, 0.0, 0.0],
               [0.0, 1.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0],
               [0.0, 0.0, 0.0, 1.0] ]
    for i, coordinate in enumerate(view_direction):
        match coordinate:
            case  "X"|"-X": matrix[i] = [ 1.0,  0.0,  0.0,  0.0]
            case  "Y"|"-Y": matrix[i] = [ 0.0,  1.0,  0.0,  0.0]
            case  "Z"|"-Z": matrix[i] = [ 0.0,  0.0,  1.0,  0.0]

    return mathutils.Matrix(matrix)



def 骨架Process():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        match 数据.变量.变换.坐标系缩放模式:
            case '自动处理': __armature__xyz__scale__to__auto__scale__(插件数据.filepath, 插件数据)
            case '原始数据': pass
            case '手动设置': __armature__xyz__scale__to__sets__scale__(插件数据)

def 网格Process():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        match 数据.变量.变换.坐标系缩放模式:
            case '自动处理': __mesh__xyz__scale__to__auto__scale__(插件数据.filepath, 插件数据)
            case '原始数据': pass
            case '手动设置': __mesh__xyz__scale__to__sets__scale__(插件数据)

def 姿态Process():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        match 数据.变量.变换.坐标系缩放模式:
            case '自动处理': __action__xyz__scale__to__auto__scale__(插件数据.filepath, 插件数据)
            case '原始数据': pass
            case '手动设置': __action__xyz__scale__to__sets__scale__(插件数据)




def __armature__xyz__scale__to__auto__scale__(filepath, 插件数据):
    match os.path.splitext(filepath)[-1]:
        case ".fbx"  : __骨架__手动处理__位置坐标缩放__(1.00, 插件数据.文件骨架)
        case ".nif"  : __骨架__手动处理__位置坐标缩放__(0.01, 插件数据.文件骨架)
        case ".xac"  : __骨架__手动处理__位置坐标缩放__(0.01, 插件数据.文件骨架)
        case ".vmesh": __骨架__手动处理__位置坐标缩放__(0.01, 插件数据.文件骨架)
        case ".model": __骨架__手动处理__位置坐标缩放__(0.01, 插件数据.文件骨架)
        case ".srt"  : __骨架__手动处理__位置坐标缩放__(0.01, 插件数据.文件骨架)

def __mesh__xyz__scale__to__auto__scale__(filepath, 插件数据):
    match os.path.splitext(filepath)[-1]:
        case ".fbx"  : __网格__手动处理__位置坐标缩放__(1.00, 插件数据)
        case ".nif"  : __网格__手动处理__位置坐标缩放__(0.01, 插件数据)
        case ".xac"  : __网格__手动处理__位置坐标缩放__(0.01, 插件数据)
        case ".vmesh": __网格__手动处理__位置坐标缩放__(0.01, 插件数据)
        case ".model": __网格__手动处理__位置坐标缩放__(0.01, 插件数据)
        case ".srt"  : __网格__手动处理__位置坐标缩放__(0.01, 插件数据)


def __action__xyz__scale__to__auto__scale__(filepath, 插件数据):
    match os.path.splitext(filepath)[-1]:
        case ".fbx"  : 
            __姿态__手动处理__位置坐标缩放__(1.00, 插件数据.文件姿态)
            __姿态__手动处理__位置坐标缩放__(1.00, 数据.变量.选择集.文件姿态)
        case ".kf"   : 
            __姿态__手动处理__位置坐标缩放__(0.01, 插件数据.文件姿态)
            __姿态__手动处理__位置坐标缩放__(0.01, 数据.变量.选择集.文件姿态)
        case ".xsm"  : 
            __姿态__手动处理__位置坐标缩放__(0.01, 插件数据.文件姿态)
            __姿态__手动处理__位置坐标缩放__(0.01, 数据.变量.选择集.文件姿态)
        case ".hka"  : 
            __姿态__手动处理__位置坐标缩放__(0.01, 插件数据.文件姿态)
            __姿态__手动处理__位置坐标缩放__(0.01, 数据.变量.选择集.文件姿态)
        case ".hkx"  : 
            __姿态__手动处理__位置坐标缩放__(1.00, 插件数据.文件姿态)
            __姿态__手动处理__位置坐标缩放__(1.00, 数据.变量.选择集.文件姿态)



def __armature__xyz__scale__to__sets__scale__(插件数据):
    scale_value = float(数据.变量.变换.缩放系数)
    __骨架__手动处理__位置坐标缩放__(scale_value, 插件数据.文件骨架)


def __mesh__xyz__scale__to__sets__scale__(插件数据):
    scale_value = float(数据.变量.变换.缩放系数)
    __网格__手动处理__位置坐标缩放__(scale_value, 插件数据)

def __action__xyz__scale__to__sets__scale__(插件数据):
    scale_value = float(数据.变量.变换.缩放系数)
    __姿态__手动处理__位置坐标缩放__(scale_value, 插件数据.文件姿态)
    __姿态__手动处理__位置坐标缩放__(scale_value, 数据.变量.选择集.文件姿态)



def __骨架__手动处理__位置坐标缩放__(scale_value, 文件骨架):
    if 文件骨架 == None: return None
    for 骨骼名称, 文件骨骼 in 文件骨架.骨骼字典.items():
        文件骨骼.location = scale_value*文件骨骼.location # mathutils.Vector([scale_value*vx, scale_value*vy, scale_value*vz])


def __网格__手动处理__位置坐标缩放__(scale_value, 插件数据):
    for 插件网格 in 插件数据.插件网格列表:
        for i, 顶点位置 in enumerate(插件网格.顶点列表): 
            插件网格.顶点列表[i] = scale_value*顶点位置

        for 形态名称, slidermin, slidermax, 形态键 in 插件网格.形态键列表:
            for i, 顶点位置 in enumerate(形态键): 形态键[i] = scale_value*顶点位置


def __姿态__手动处理__位置坐标缩放__(scale_value, 文件姿态):
    if 文件姿态 == None: return None
    for 骨骼名称, 姿态骨骼 in 文件姿态.骨骼字典.items():
        for i, [frame, position] in enumerate(姿态骨骼.位置帧列表): 
            姿态骨骼.位置帧列表[i][1] = scale_value*position
  






