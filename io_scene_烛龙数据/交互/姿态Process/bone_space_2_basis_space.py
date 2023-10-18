
import mathutils


def location(软件armature, 文件姿态, 插件姿态):
    for pbone in 软件armature.pose.bones:
        if pbone.name not in 插件姿态.骨骼字典: continue
        姿态骨骼 = 文件姿态.骨骼字典[pbone.name]
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]

        location = mathutils.Vector(pbone.bone.head)
        if pbone.parent:
            location.y += pbone.bone.parent.length
        for time, position in 姿态骨骼.位置帧列表:
            loc = position - location
            插件骨骼.位置帧列表.append( [time, loc] )


def rotation_quaternion(软件armature, 文件姿态, 插件姿态):
    for pbone in 软件armature.pose.bones:
        if pbone.name not in 插件姿态.骨骼字典: continue
        姿态骨骼 = 文件姿态.骨骼字典[pbone.name]
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]

        rotation_quaternion = pbone.bone.matrix.to_quaternion()
        for time, quaternion in 姿态骨骼.旋转帧列表:
            quat = rotation_quaternion.conjugated() @ quaternion
            插件骨骼.旋转帧列表.append( [time, quat] )


def scale(软件armature, 文件姿态, 插件姿态):
    for pbone in 软件armature.pose.bones:
        if pbone.name not in 文件姿态.骨骼字典: continue
        姿态骨骼 = 文件姿态.骨骼字典[pbone.name]
        插件骨骼 = 插件姿态.骨骼字典[pbone.name]

        for time, scale in 姿态骨骼.缩放帧列表:
            scale = scale - pbone.scale
            插件骨骼.缩放帧列表.append( [time, scale] )