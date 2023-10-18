import os
import bpy
import math
import mathutils
from . import struct
from ... import 数据, 接口


class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath       
        self.文件骨架 = self.骨架处理(filedata)
        self.文件姿态 = self.姿态处理(filedata)
        pass


    def 骨架处理(self, filedata):
        文件骨架 = 接口.结构.文件骨架()
        for name, o in filedata.bone_dict.items(): # 所有model对象都当骨骼处理
            文件骨骼 = 文件骨架.骨骼()
            文件骨骼.name = o.name
            文件骨骼.parentname = o.parent.name if o.parent != None else ""
            location = mathutils.Vector(o.translation) if o.translation != [] else None
            euler = mathutils.Euler( (math.radians(o.rotation[0]), math.radians(o.rotation[1]), math.radians(o.rotation[2])), 'XYZ' ) if o.rotation != [] else None
            scale = mathutils.Vector(o.scale) if o.scale != [] else None
            文件骨骼.matrix_local = mathutils.Matrix.LocRotScale(location, euler, scale) # mathutils.Matrix.LocRotScale() 接受None
            if 文件骨骼.parentname != "": 文件骨骼.matrix_local = 文件骨架.骨骼字典[文件骨骼.parentname].matrix_local @ 文件骨骼.matrix_local 
            文件骨架.骨骼字典[o.name] = 文件骨骼
        return 文件骨架
    


    def 姿态处理(self, filedata): # 字典转列表
        文件姿态 = 接口.结构.文件姿态()
        for name, o in filedata.bone_dict.items():
            文件骨骼 = 文件姿态.骨骼()
            文件骨骼.名称 = name
            for time, [vx, vy, vz] in o.action_translation.items():
                文件骨骼.位置帧列表.append( [time, mathutils.Vector([vx, vy, vz])] )

            for time, [rx, ry, rz] in o.action_rotation.items():
                euler = mathutils.Euler( (math.radians(rx), math.radians(ry), math.radians(rz)), 'XYZ' )
                文件骨骼.旋转帧列表.append( [time, euler.to_quaternion()] )

            # for time, [sx, sy, sz] in o.action_scale.items():
            #     文件骨骼.缩放帧列表.append( [time, mathutils.Vector([sx, sy, sz])] )
            # 加进来数据异常，骨骼消失

            文件姿态.骨骼字典[name] = 文件骨骼
        return 文件姿态


