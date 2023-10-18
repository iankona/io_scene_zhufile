# https://github.com/CucFlavius/Zee-010-Templates/blob/main/HKSplineCompressedAnimation.bt
# https://github.com/CucFlavius/Zee-010-Templates/blob/main/FFXIV_PAP.bt_bak
# https://github.com/Meowmaritus/SoulsAssetPipeline/blob/master/SoulsAssetPipeline/Animation/HKX/SplineCompressedAnimation.cs

import os
import bpy
import math
import mathutils
from . import struct
from ... import 接口


class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath     
        self.文件姿态 = self.动作处理(filedata)


    def 动作处理(self, filedata):
        文件姿态 = 接口.结构.文件姿态()
        for 骨骼名称, 位置帧列表, 旋转帧列表, 缩放帧列表, 旋转缩放帧列表 in filedata.ACTI.骨骼节点列表:
            文件骨骼 = 文件姿态.骨骼()
            文件骨骼.名称 = 骨骼名称
            for [vx, vy, vz], time in 位置帧列表:
                文件骨骼.位置帧列表.append([time, mathutils.Vector([vx, vy, vz])])
            for [qx, qy, qz, qw], time in 旋转帧列表:
                文件骨骼.旋转帧列表.append([time, mathutils.Quaternion([qw, qx, qy, qz])])
            for [sx, sy, sz], time in 缩放帧列表:
                文件骨骼.缩放帧列表.append([time, mathutils.Vector([sx, sy, sz])])
            文件姿态.骨骼字典[骨骼名称] = 文件骨骼
        return 文件姿态
















