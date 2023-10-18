
import mathutils
from ... import 数据





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



def 姿态通道_位置变换(view_direction, 插件姿态):
    coordinate_matrix = coordinate_system_transformation_matrix(view_direction)
    for 骨骼名称, 姿态骨骼 in 插件姿态.骨骼字典.items():
        for i, [time, position] in enumerate(姿态骨骼.位置帧列表):
            姿态骨骼.位置帧列表[i][1] = coordinate_matrix @ position  



def 姿态通道_骨骼轴向变换(view_direction, 插件姿态):
    coordinate_matrix = coordinate_system_transformation_matrix(view_direction)
    for 骨骼名称, 姿态骨骼 in 插件姿态.骨骼字典.items():
        for i, [time, rotation] in enumerate(姿态骨骼.旋转帧列表): # 直接 coordinate_matrix @ rotation 达不到预计的效果，估计只有位置变换，没有骨骼轴向变换
            qw, qx, qy, qz = rotation
            qx, qy, qz = coordinate_matrix @ mathutils.Vector([qx, qy, qz])
            姿态骨骼.旋转帧列表[i][1] = mathutils.Quaternion([qw, qx, qy, qz])  


def 姿态通道_位置缩放(scale_vec3, 插件姿态):
    scale_matrix = mathutils.Matrix.LocRotScale(None, None, scale_vec3)
    for 骨骼名称, 姿态骨骼 in 插件姿态.骨骼字典.items():
        for i, [time, scale] in enumerate(姿态骨骼.缩放帧列表):
            姿态骨骼.缩放帧列表[i][1] = scale_matrix @ scale