# https://github.com/CucFlavius/Zee-010-Templates/blob/main/HKSplineCompressedAnimation.bt
# https://github.com/CucFlavius/Zee-010-Templates/blob/main/FFXIV_PAP.bt_bak
# https://github.com/Meowmaritus/SoulsAssetPipeline/blob/master/SoulsAssetPipeline/Animation/HKX/SplineCompressedAnimation.cs

import os
import bpy
import math
import mathutils
from . import struct
from ... import 数据, 接口, 工具, 文件

class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath       
        self.文件骨架 = self.骨架处理(filedata)
        self.表情读取(filedata)
        self.形态键列表 = self.表情处理(filedata)
        self.权重处理(filedata)
        self.插件材质列表 = self.材质处理(filedata)
        self.插件网格列表 = self.模型处理(filedata)


    def 表情读取(self, filedata):
        if "morphface.model"  not in filedata.filepath: return ""
        filepath = filedata.filepath[0:-6] + ".morph"
        bp = 文件.bpformat.bpnumpy.类().filepath(filepath)
        filedata.STCM = 文件.morph.类(bp).STCM
        bp.close()


    def 表情处理(self, filedata):
        if "STCM" not in filedata.__dict__: return []
        形态键列表 = []
        match 数据.变量.古剑3选项.表情导入模式:
            case "形态键左值": 形态键列表 = self.__形态键左值__(filedata)
            case "形态键右值": 形态键列表 = self.__形态键右值__(filedata)
            case "形态键均值": 形态键列表 = self.__形态键均值__(filedata)
        return 形态键列表


    def 骨架处理(self, filedata):
        if "LEKS" not in filedata.__dict__: return None
        文件骨架 = 接口.结构.文件骨架()
        for [骨骼名称, parentindex, [vx, vy, vz], [qx, qy, qz, qw], head_res, rotation_quaternion_res ] in filedata.LEKS.骨骼节点列表:
            文件骨骼 = 文件骨架.骨骼()
            文件骨骼.name = 骨骼名称
            文件骨骼.parentname = filedata.LEKS.骨骼节点列表[parentindex][0] if parentindex != -1 else ""
            文件骨骼.matrix_local = mathutils.Quaternion([qw, qx, qy, qz]).to_matrix().to_4x4() @ mathutils.Matrix.Translation(mathutils.Vector([-vx, -vy, -vz]))
            文件骨架.骨骼字典[骨骼名称] = 文件骨骼
        return 文件骨架
    

    # def 骨架处理RES(self, filedata):
    #     if "LEKS" not in filedata.__dict__: return ""
    #     文件骨架 = 接口.结构.文件骨架()
    #     for [骨骼名称, parentindex, head, rotation_quaternion, [vx, vy, vz], [qx, qy, qz, qw] ] in filedata.LEKS.骨骼节点列表:
    #         文件骨骼 = 文件骨架.骨骼()
    #         文件骨骼.name = 骨骼名称
    #         文件骨骼.parentname = filedata.LEKS.骨骼节点列表[parentindex][0] if parentindex != -1 else ""
    #         文件骨骼.matrix_local = mathutils.Matrix.LocRotScale(mathutils.Vector([-vx, vz, -vy]), mathutils.Quaternion([qw, qx, qy, qz]), None)
    #         if 文件骨骼.parentname != "":
    #             文件骨骼.matrix_local = 文件骨架.骨骼字典[文件骨骼.parentname].matrix_local @ 文件骨骼.matrix_local

    #         文件骨架.骨骼字典[骨骼名称] = 文件骨骼
    #     return 文件骨架
    
    
    def 材质处理(self, filedata):
        插件材质列表 = []
        for lrtm in filedata.SRTM.材质列表:
            插件材质 = 接口.结构.插件材质()
            插件材质.名称 = lrtm.材质名称 # Material #49/<g3_cloth2>actress2_bx_body , 'Material #6388/<cloth><g3_cloth2>actress1_md_body'
            插件材质.标签贴图相对地址列表 = self.__贴图处理__(lrtm.相对贴图地址列表)
            插件材质列表.append(插件材质)
        return 插件材质列表


    def 权重处理(self, filedata):
        # boneid -> bonename
        if "THGW" not in filedata.__dict__: return ""
        for 权重组 in filedata.THGW.顶点骨骼组列表:
            for i, [骨骼ID, 权重值] in enumerate(权重组):
                骨骼名称 = filedata.LEKS.骨骼节点列表[骨骼ID][0]
                权重组[i] = [骨骼名称, 权重值]


    def 模型处理(self, filedata):
        插件网格列表 = []
        for i, [loop左值, loop个数, vert左值, vert个数, 材质索引] in enumerate(filedata.MBUS.顶点划分信息列表) :
            插件网格 = 接口.结构.插件网格()
            插件网格.插件材质 = self.插件材质列表[材质索引]
            插件网格.顶点列表 = [mathutils.Vector(position) for position in filedata.HSMV.mesh.顶点列表[vert左值: vert左值+vert个数]]
            插件网格.顶点UV列表 = filedata.HSMV.mesh.顶点UV列表[vert左值: vert左值+vert个数]
            插件网格.顶点Loop列表 = [ loop个值-vert左值 for loop个值 in filedata.HSMV.mesh.顶点Loop列表[loop左值: loop左值+loop个数] ]
            if "THGW" in filedata.__dict__:
                if filedata.THGW.顶点骨骼组列表 != []:
                    插件网格.骨骼组列表 = filedata.THGW.顶点骨骼组列表[vert左值: vert左值+vert个数]
            for 形态键名称, slidermin, slidermax, 新顶点列表 in self.形态键列表:
                形态顶点列表 = [mathutils.Vector(position) for position in 新顶点列表[vert左值: vert左值+vert个数]]
                插件网格.形态键列表.append( [形态键名称, slidermin, slidermax, 形态顶点列表] )

            if 数据.变量.网格.导入缺UV网格 == False:
                if 插件网格.顶点UV列表 == []: continue    
            插件网格列表.append(插件网格)
        return 插件网格列表


    def __形态键左值__(self, filedata):
        形态键列表 = []
        slidermin, slidermax = 0, 1
        形态键列表.append([ "morph_0", slidermin, slidermax, filedata.HSMV.mesh.顶点列表[:] ])
        for 形态键名称, 相对顶点列表 in filedata.STCM.形态键列表:
            新顶点列表 = filedata.HSMV.mesh.顶点列表[:]
            for index, leftlocation, rightlocation in 相对顶点列表:
                x1, y1, z1 = 新顶点列表[index]
                x2, y2, z2 = leftlocation
                新顶点列表[index] = [x1+x2, y1+y2, z1+z2]
            形态键列表.append([形态键名称, slidermin, slidermax, 新顶点列表])
        return 形态键列表


    def __形态键右值__(self, slidermin=0, slidermax=1, filedata=None, ):
        形态键列表 = []
        slidermin, slidermax = -1, 0
        形态键列表.append([ "morph_0", slidermin, slidermax, filedata.HSMV.mesh.顶点列表[:] ])
        for 形态键名称, 相对顶点列表 in filedata.STCM.形态键列表:
            新顶点列表 = filedata.HSMV.mesh.顶点列表[:]
            for index, leftlocation, rightlocation in 相对顶点列表:
                x1, y1, z1 = 新顶点列表[index]
                x3, y3, z3 = rightlocation
                新顶点列表[index] = [x1+x3, y1+y3, z1+z3]
            形态键列表.append([形态键名称, slidermin, slidermax, 新顶点列表])
        return 形态键列表

    def __形态键均值__(self, filedata):
        形态键列表 = []
        slidermin, slidermax = -0.5, 0.5
        形态键列表.append([ "morph_0", slidermin, slidermax, filedata.HSMV.mesh.顶点列表[:] ])
        for 形态键名称, 相对顶点列表 in filedata.STCM.形态键列表:
            新顶点列表 = filedata.HSMV.mesh.顶点列表[:]
            for index, leftlocation, rightlocation in 相对顶点列表:
                    x1, y1, z1 = 新顶点列表[index]
                    x2, y2, z2 = leftlocation
                    x3, y3, z3 = rightlocation
                    x0, y0, z0 = (x2+x3)/2, (y2+y3)/2, (z2+z3)/2
                    新顶点列表[index] = [x1+x0, y1+y0, z1+z0]
            形态键列表.append([形态键名称, slidermin, slidermax, 新顶点列表])
        return 形态键列表

    def __贴图处理__(self, 贴图相对地址列表): # ['..\\textures\\actress1_md_body_01d.tga', '..\\textures\\actress1_md_body_01s.tga', '..\\textures\\actress1_md_body_01n.tga', '..\\textures\\actress1_md_body_01m.tga']
        贴图相对地址列表 = [relpath[0:-4]+".dds" for relpath in 贴图相对地址列表]
        贴图标签列表 = []
        for 贴图地址 in 贴图相对地址列表:
            match 贴图地址[-5:-4]:
                case "d": 贴图标签 = "基础色"
                case "s": 贴图标签 = "高光"
                case "n": 贴图标签 = "法向"
                case "m": 贴图标签 = "糙度"
                case  _ : 贴图标签 = "其他"
            贴图标签列表.append([贴图标签, 贴图地址])
        return 贴图标签列表
    


