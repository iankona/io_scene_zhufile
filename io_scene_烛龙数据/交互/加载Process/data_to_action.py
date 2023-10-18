import os
import bpy
import math
import mathutils
from ... import 数据




def 骨架新建动作(软件armatureobj, action_name):
    软件armatureobj.animation_data_clear()
    软件armatureobj.animation_data_create()
    软件armatureobj.animation_data.action = bpy.data.actions.new(action_name)


def 骨架更换动作(软件armatureobj, action_name):
    软件armatureobj.animation_data_clear() # claer() 后 armatureobj.animation_data.action = action # AttributeError: 'NoneType' object has no attribute 'action'
    软件armatureobj.animation_data_create()
    if action_name not in bpy.data.actions: return None
    软件armatureobj.animation_data.action = bpy.data.actions[action_name]


def 骨架添加位置帧(软件armatureobj, 插件姿态):
    for pbone in 软件armatureobj.pose.bones:
        if pbone.name not in 插件姿态.骨骼字典: continue
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]

        for time, location in 插件骨骼.位置帧列表:
            pbone.location = location
            pbone.keyframe_insert("location", frame=time)


def 骨架添加旋转帧(软件armatureobj, 插件姿态):
    for pbone in 软件armatureobj.pose.bones:
        if pbone.name not in 插件姿态.骨骼字典: continue
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]

        for time, quaternion in 插件骨骼.旋转帧列表:
            pbone.rotation_quaternion = quaternion
            pbone.keyframe_insert("rotation_quaternion", frame=time)

def 骨架添加缩放帧(软件armatureobj, 插件姿态):
    for pbone in 软件armatureobj.pose.bones:
        if pbone.name not in 插件姿态.骨骼字典: continue
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]


        for time, scale in 插件骨骼.缩放帧列表:
            pbone.scale = scale
            pbone.keyframe_insert("scale", frame=time)



