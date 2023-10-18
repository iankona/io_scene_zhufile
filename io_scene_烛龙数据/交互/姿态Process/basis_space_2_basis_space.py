
import mathutils


def location(软件armature, 文件姿态, 插件姿态):
    for pbone in 软件armature.pose.bones:
        if pbone.name not in 插件姿态.骨骼字典: continue
        姿态骨骼 = 文件姿态.骨骼字典[pbone.name]
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]
        插件骨骼.位置帧列表 = 姿态骨骼.位置帧列表[:]


def rotation_quaternion(软件armature, 文件姿态, 插件姿态):
    for pbone in 软件armature.pose.bones:
        if pbone.name not in 插件姿态.骨骼字典: continue
        姿态骨骼 = 文件姿态.骨骼字典[pbone.name]
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]
        插件骨骼.旋转帧列表 = 姿态骨骼.旋转帧列表[:]


def scale(软件armature, 文件姿态, 插件姿态):
    for pbone in 软件armature.pose.bones:
        if pbone.name not in 文件姿态.骨骼字典: continue
        姿态骨骼 = 文件姿态.骨骼字典[pbone.name]
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]
        插件骨骼.缩放帧列表 = 姿态骨骼.缩放帧列表[:]