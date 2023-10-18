import os
import mathutils

from . import loc_basis_coordinate_process
from ... import 数据




def 通道坐标系变换_各自处理():
    __通道坐标系变换__各自处理__选择骨架__()
    __通道坐标系变换__各自处理__姿态骨架__()



def __通道坐标系变换__各自处理__选择骨架__():
    # if 数据.变量.选择骨架and插件姿态列表 == []: return None # 和for重复
    for 软件armatureobj, 插件姿态列表 in 数据.变量.选择骨架and插件姿态列表:
        for filepath, 文件姿态, 插件姿态 in 插件姿态列表: 
            __位置通道__Basis空间__位置变换__(filepath, 插件姿态)
            __旋转通道__Basis空间__旋转变换__(filepath, 插件姿态) # 骨骼轴向变换
            __缩放通道__Basis空间__缩放变换__(filepath, 插件姿态)

    
def __通道坐标系变换__各自处理__姿态骨架__():         
    # if 数据.变量.姿态骨架and插件姿态列表 == []: return None
    for 软件armatureobj, 插件姿态列表 in 数据.变量.姿态骨架and插件姿态列表:
        for filepath, 文件姿态, 插件姿态 in 插件姿态列表: 
            __位置通道__Basis空间__位置变换__(filepath, 插件姿态)
            __旋转通道__Basis空间__旋转变换__(filepath, 插件姿态) # 骨骼轴向变换
            __缩放通道__Basis空间__缩放变换__(filepath, 插件姿态)



def __位置通道__Basis空间__位置变换__(filepath, 插件姿态):
    match 数据.变量.姿态通道位置.坐标系变换模式:
        case '自动处理': __basis__space__location__coordinate__auto__convert__(filepath, 插件姿态)
        case '原始数据': pass
        case '手动设置': __basis__space__location__coordinate__sets__convert__(插件姿态)

def __旋转通道__Basis空间__旋转变换__(filepath, 插件姿态): # 骨骼轴向变换
    match 数据.变量.姿态通道旋转.坐标系变换模式:
        case '自动处理': __basis__space__rotation__coordinate__auto__convert__(filepath, 插件姿态)
        case '原始数据': pass
        case '手动设置': __basis__space__rotation__coordinate__sets__convert__(插件姿态)

def __缩放通道__Basis空间__缩放变换__(filepath, 插件姿态):
    match 数据.变量.姿态通道缩放.坐标系缩放模式:
        case '自动处理': __basis__space__scale__coordinate__auto__convert__(filepath, 插件姿态)
        case '原始数据': pass
        case '手动设置': __basis__space__scale__coordinate__sets__convert__(插件姿态)


def __basis__space__location__coordinate__auto__convert__(filepath, 插件姿态):
    # blender 3dview 空间 [X, Y, Z] == blender basis 空间 [X, Z, -Y]
    match os.path.splitext(filepath)[-1]:
        case ".fbx": loc_basis_coordinate_process.姿态通道_位置变换(["Y", "Z", "-X"], 插件姿态)
        case ".hka": pass
        case ".hkx": loc_basis_coordinate_process.姿态通道_位置变换(["Y", "Z", "-X"], 插件姿态)


def __basis__space__rotation__coordinate__auto__convert__(filepath, 插件姿态):
    match os.path.splitext(filepath)[-1]:
        case ".fbx": pass
        case ".hka": pass
        case ".hkx": pass            


def __basis__space__scale__coordinate__auto__convert__(filepath, 插件姿态):
    match os.path.splitext(filepath)[-1]:
        case ".fbx": pass
        case ".hka": pass
        case ".hkx": pass


def __basis__space__location__coordinate__sets__convert__(插件姿态):
    view_direction = [数据.变量.姿态通道位置.坐标系向前, 数据.变量.姿态通道位置.坐标系向右, 数据.变量.姿态通道位置.坐标系向上]
    loc_basis_coordinate_process.姿态通道_位置变换(view_direction, 插件姿态)


def __basis__space__rotation__coordinate__sets__convert__(插件姿态):
    view_direction = [数据.变量.姿态通道旋转.坐标系向前, 数据.变量.姿态通道旋转.坐标系向右, 数据.变量.姿态通道旋转.坐标系向上]
    loc_basis_coordinate_process.姿态通道_骨骼轴向变换(view_direction, 插件姿态)
       

def __basis__space__scale__coordinate__sets__convert__(插件姿态):
    scale_vec3 = mathutils.Vector([数据.变量.姿态通道缩放.scale_x, 数据.变量.姿态通道缩放.scale_y, 数据.变量.姿态通道缩放.scale_z])
    loc_basis_coordinate_process.姿态通道_位置缩放(scale_vec3, 插件姿态)



