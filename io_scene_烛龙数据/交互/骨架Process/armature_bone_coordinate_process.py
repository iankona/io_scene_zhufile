import bpy
import math
import mathutils
from ... import 数据, 接口, 工具


def coordinate_system_transformation_matrix(view_direction=["-Y", "X", "Z"]):
    matrix = [ [1.0, 0.0, 0.0, 0.0],
               [0.0, 1.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0],
               [0.0, 0.0, 0.0, 1.0] ]
    for i, coordinate in enumerate(view_direction):
        match coordinate:
            case  "X": matrix[i] = [ 1.0,  0.0,  0.0,  0.0]
            case "-X": matrix[i] = [-1.0,  0.0,  0.0,  0.0]
            case  "Y": matrix[i] = [ 0.0,  1.0,  0.0,  0.0]
            case "-Y": matrix[i] = [ 0.0, -1.0,  0.0,  0.0]
            case  "Z": matrix[i] = [ 0.0,  0.0,  1.0,  0.0]
            case "-Z": matrix[i] = [ 0.0,  0.0, -1.0,  0.0]

    return mathutils.Matrix(matrix)

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



def 骨架位置_手动处理_坐标变换(coordinate_matrix, 文件骨架):
    for 骨骼名称, 文件骨骼 in 文件骨架.骨骼字典.items():
        loc, quat, scale = 文件骨骼.matrix_local.decompose()
        loc = coordinate_matrix @ loc
        文件骨骼.matrix_local = mathutils.Matrix.LocRotScale(loc, quat, scale)


def 骨架旋转_手动处理_坐标变换(coordinate_matrix, 文件骨架):
    for 骨骼名称, 文件骨骼 in 文件骨架.骨骼字典.items():
        loc, quat, scale = 文件骨骼.matrix_local.decompose()
        matrix = coordinate_matrix @ quat.to_matrix().to_4x4()
        quat = matrix.to_quaternion()
        文件骨骼.matrix_local = mathutils.Matrix.LocRotScale(loc, quat, scale)


def 骨架缩放_手动处理_坐标变换(scale_matrix, 文件骨架):
    for 骨骼名称, 文件骨骼 in 文件骨架.骨骼字典.items():   
        loc, quat, scale = 文件骨骼.matrix_local.decompose()
        scale = scale_matrix @ scale
        文件骨骼.matrix_local = mathutils.Matrix.LocRotScale(loc, quat, scale)