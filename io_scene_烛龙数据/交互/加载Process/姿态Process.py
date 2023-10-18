import os
import bpy
import math
import mathutils
from ... import 数据

from .   import data_to_action




def 新建action():
    __新建action__选择骨架__()
    __新建action__姿态骨架__()



def __新建action__选择骨架__():
    for 软件armatureobj, 插件姿态列表 in 数据.变量.选择骨架and插件姿态列表:
        for filepath, 文件姿态, 插件姿态 in 插件姿态列表:
            action_name = f"{软件armatureobj.name}_{os.path.basename(filepath)}"
            match 数据.变量.姿态.动画导入模式:
                case '引用现有Action': data_to_action.骨架更换动作(软件armatureobj, action_name)
                case '新建单独Action': data_to_action.骨架新建动作(软件armatureobj, action_name)
            if "Loc" in 数据.变量.姿态.动作导入通道: data_to_action.骨架添加位置帧(软件armatureobj, 插件姿态)
            if "Rot" in 数据.变量.姿态.动作导入通道: data_to_action.骨架添加旋转帧(软件armatureobj, 插件姿态)
            if "Sca" in 数据.变量.姿态.动作导入通道: data_to_action.骨架添加缩放帧(软件armatureobj, 插件姿态)


def __新建action__姿态骨架__():
    for 软件armatureobj, 插件姿态列表 in 数据.变量.姿态骨架and插件姿态列表:
        for filepath, 文件姿态, 插件姿态 in 插件姿态列表:
            action_name = f"{软件armatureobj.name}_{os.path.basename(filepath)}"
            match 数据.变量.姿态.动画导入模式:
                case '引用现有Action': data_to_action.骨架更换动作(软件armatureobj, action_name)
                case '新建单独Action': data_to_action.骨架新建动作(软件armatureobj, action_name)
            if "Loc" in 数据.变量.姿态.动作导入通道: data_to_action.骨架添加位置帧(软件armatureobj, 插件姿态)
            if "Rot" in 数据.变量.姿态.动作导入通道: data_to_action.骨架添加旋转帧(软件armatureobj, 插件姿态)
            if "Sca" in 数据.变量.姿态.动作导入通道: data_to_action.骨架添加缩放帧(软件armatureobj, 插件姿态)





