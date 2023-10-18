# https://github.com/CucFlavius/Zee-010-Templates/blob/main/HKSplineCompressedAnimation.bt
# https://github.com/CucFlavius/Zee-010-Templates/blob/main/FFXIV_PAP.bt_bak
# https://github.com/Meowmaritus/SoulsAssetPipeline/blob/master/SoulsAssetPipeline/Animation/HKX/SplineCompressedAnimation.cs

import os
import bpy
import math
import mathutils
from . import struct
from ... import 数据, 接口, 工具


class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath    
        self.骨骼节点列表 = []
        self.节点处理(filedata)
        self.设置处理()
        self.文件姿态 = self.动作处理()


    def 节点处理(self, filedata):
        # 1 NiTransformEvaluator --> 1 NiTransformData  # 一一对应
        NiTransformEvaluators = []
        NiTransformDatas = []
        for o in filedata.datas:
            classtypename = str(type(o))
            classname = classtypename.split(".")[-2]
            if "NiTransformEvaluator" in classname: 
                o.NiTransformData = filedata.datas[o.NiTransformDataID]
                NiTransformEvaluators.append(o)
            if "NiTransformData" in classname: NiTransformDatas.append(o)


        for NiTransformData in NiTransformDatas:
            if NiTransformData.旋转曲线帧列表 == []: continue

            fcurve_x, fcurve_y, fcurve_z = NiTransformData.旋转曲线帧列表
            NiTransformData.旋转曲线帧列表 = []
            for [frame, radian_x], [frame, radian_y], [frame, radian_z] in zip(fcurve_x, fcurve_y, fcurve_z):
                euler = mathutils.Euler((radian_x, radian_y, radian_z), 'XYZ')
                quat  = euler.to_quaternion()
                NiTransformData.旋转曲线帧列表.append( [frame, quat] )

        for NiTransformEvaluator in NiTransformEvaluators:
            if NiTransformEvaluator.NiTransformData.type != "NiTransformData": continue  # 类名还有另外的'NiTextKeyExtraData'
            self.骨骼节点列表.append( [
                NiTransformEvaluator.name, 
                NiTransformEvaluator.NiTransformData.位置帧列表,
                NiTransformEvaluator.NiTransformData.旋转帧列表,
                NiTransformEvaluator.NiTransformData.缩放帧列表,
                NiTransformEvaluator.NiTransformData.旋转曲线帧列表,
                ] )


    def 设置处理(self):
        if 数据.变量.古剑1选项.导入头发裙子动画 == False: return None
        for i, [骨骼名称, 位置帧列表, 旋转帧列表, 缩放帧列表, 旋转曲线帧列表] in enumerate(self.骨骼节点列表):
            if 旋转帧列表 == [] and 旋转曲线帧列表 != []: self.骨骼节点列表[i][2] = self.骨骼节点列表[i][4]
            if 旋转帧列表 != [] and 旋转曲线帧列表 != []:
                time_set = set()
                旋转帧字典, 旋转曲线帧字典 = {}, {}
                for time, [qw, qx, qy, qz] in 旋转帧列表:
                    time_set.add(round(time))
                    旋转帧字典[round(time)] = mathutils.Quaternion([qw, qx, qy, qz])
                for time, [qw, qx, qy, qz] in 旋转曲线帧列表:
                    time_set.add(round(time))
                    旋转曲线帧字典[round(time)] = mathutils.Quaternion([qw, qx, qy, qz])
                
                旋转帧列表 = [] # list(集合) 将自动返回1个排序列表（默认升序）
                for time in list(time_set):
                    if time in 旋转帧字典: 
                        quat1 = 旋转帧字典[time]
                    else:
                        quat1 = mathutils.Quaternion() # Quaternion((1.0, 0.0, 0.0, 0.0))
                    if time in 旋转曲线帧字典: 
                        quat2 = 旋转曲线帧字典[time]
                    else:
                        quat2 = mathutils.Quaternion() # Quaternion((1.0, 0.0, 0.0, 0.0))
                    旋转帧列表.append([time, quat2 @ quat1])
                self.骨骼节点列表[i][2] = 旋转帧列表



    def 动作处理(self):
        文件姿态 = 接口.结构.文件姿态()
        for 骨骼名称, 位置帧列表, 旋转帧列表, 缩放帧列表, 旋转曲线帧列表 in self.骨骼节点列表:
            文件骨骼 = 文件姿态.骨骼()
            文件骨骼.名称 = 骨骼名称
            for time, [vx, vy, vz] in 位置帧列表:
                文件骨骼.位置帧列表.append([time, mathutils.Vector([vx, vy, vz])])
            for time, [qw, qx, qy, qz] in 旋转帧列表:
                文件骨骼.旋转帧列表.append([time, mathutils.Quaternion([qw, qx, qy, qz])])
            for time, [sx, sy, sz] in 缩放帧列表:
                文件骨骼.缩放帧列表.append([time, mathutils.Vector([sx, sy, sz])])
            文件姿态.骨骼字典[骨骼名称] = 文件骨骼
        return 文件姿态


















