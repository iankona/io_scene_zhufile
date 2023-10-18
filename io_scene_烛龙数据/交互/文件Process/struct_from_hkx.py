import os
import mathutils
from . import struct
from ... import 数据, 接口


class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath        
        self.文件姿态 = self.姿态处理(filedata)


    def 姿态处理(self, filedata):
        文件姿态 = 接口.结构.文件姿态()
        for trackname, [trackname, positiondict, rotationdict, scaledict] in filedata.action.tracknodes.items():
            文件骨骼 = 文件姿态.骨骼()
            文件骨骼.名称 = trackname
            for time, [vx, vy, vz] in positiondict.items(): # 姿态位置[XYZ]对应的是骨架位置[-X-Y-Z]，如果对应骨架位置[XYZ]，动画导入会把模型拉成细条状
                文件骨骼.位置帧列表.append([time, mathutils.Vector([vx, vy, vz])])
            for time, [qx, qy, qz, qw] in rotationdict.items():
                文件骨骼.旋转帧列表.append([time, mathutils.Quaternion([qw, qx, qy, qz])])
            # for time, [sx, sy, sz] in scaledict.items():
            #     文件骨骼.缩放帧列表.append([time, mathutils.Vector([sx, sy, sz])])
            文件姿态.骨骼字典[trackname] = 文件骨骼
        return 文件姿态


