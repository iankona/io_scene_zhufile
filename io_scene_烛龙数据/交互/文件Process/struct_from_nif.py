# https://github.com/CucFlavius/Zee-010-Templates/blob/main/HKSplineCompressedAnimation.bt
# https://github.com/CucFlavius/Zee-010-Templates/blob/main/FFXIV_PAP.bt_bak
# https://github.com/Meowmaritus/SoulsAssetPipeline/blob/master/SoulsAssetPipeline/Animation/HKX/SplineCompressedAnimation.cs

import os
import bpy
import math
import mathutils
from . import struct
from ... import 接口, 数据


class Nif文件网格:
    def __init__(self):
        self.顶点列表 = []
        self.顶点UV列表 = []
        self.顶点Loop列表 = []
        self.形态键列表 = []
        self.权重值组列表 = []
        self.骨骼ID索引值组列表 = []
        self.骨骼ID列表索引值列表 = []
        self.骨骼ID列表索引值列表 = []

        self.顶点骨骼组列表 = []
        

class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath 
        self.节点矩阵(filedata)
        self.文件骨架 = self.骨架处理()
        self.节点网格(filedata)
        self.表情处理()
        self.权重处理(filedata)
        self.网格处理()
        self.材质处理()
        self.插件网格列表 = self.模型处理()


    def 节点矩阵(self, filedata):
        self.nodes = []
        self.meshs = []
        for o in filedata.datas:
            if o.type == "NiNode": self.nodes.append(o)
            if o.type == "NiMesh": self.meshs.append(o)
            # classtypename = str(type(o))
            # classname = classtypename.split(".")[-2]
            # if "NiNode" in classname: self.nodes.append(o)
            # if "NiMesh" in classname: self.meshs.append(o)

        for o in self.nodes+self.meshs:
            o.parent = None
            o.matrix_local = mathutils.Matrix(o.matrix).to_4x4()
            o.matrix_local.translation = mathutils.Vector(o.position)


        根节点 = self.nodes[0]
        def 遍历(parent):
            for childindex in parent.children:
                child = filedata.datas[childindex]
                if child.type == "NiNode":
                    child.parent = parent
                    child.matrix_local = parent.matrix_local @ child.matrix_local
                    遍历(child)
                if child.type == "NiMesh":
                    child.parent = parent
                    child.matrix_local = parent.matrix_local @ child.matrix_local
        遍历(根节点)


    def 骨架处理(self):
        文件骨架 = 接口.结构.文件骨架()
        for o in self.nodes:
            文件骨骼 = 文件骨架.骨骼()
            文件骨骼.name = o.名称
            文件骨骼.parentname = o.parent.名称 if o.parent is not None else ""
            文件骨骼.matrix_local = o.matrix_local
            文件骨架.骨骼字典[o.名称] = 文件骨骼
        return 文件骨架


    def 节点网格(self, filedata):
        for o in self.meshs:
            o.材质名称 = ""
            o.贴图名称列表 = []
            for 属性ID in o.属性ID列表:
                属性 = filedata.datas[属性ID]
                if 属性.type == 'NiMaterialProperty':  # 只会有1个
                    o.材质名称 = 属性.名称
                if 属性.type == 'NiTexturingProperty': # 有多个
                    for NiSourceTextureID in 属性.NiSourceTextureID列表:
                        NiSourceTexture = filedata.datas[NiSourceTextureID]
                        if NiSourceTexture.贴图名称 not in o.贴图名称列表: o.贴图名称列表.append(NiSourceTexture.贴图名称)

            o.骨骼ID列表 = []
            for 修改器ID in o.修改器ID列表:
                修改器 = filedata.datas[修改器ID]
                if 修改器.type == "NiSkinningMeshModifier":
                    o.骨骼ID列表 = 修改器.骨骼ID列表
                    break


            o.网格列表 = []
            for i in range(o.NiDataStream区域总数):
                网格 = Nif文件网格()
                o.网格列表.append(网格)


            for NiDataStreamID, 标识列表 in o.NiDataStreamID列表:
                NiDataStream = filedata.datas[NiDataStreamID]
                for 网格, 描述列表 in zip(o.网格列表, NiDataStream.描述列表列表):
                    for [标识, 编号], 列表 in zip(标识列表, 描述列表):
                        if 标识 == 'INDEX': 网格.顶点Loop列表 = 列表
                        if 标识 == 'POSITION': 网格.顶点列表 = 列表
                        if 标识 == 'POSITION_BP': 网格.顶点列表 = 列表
                        if 标识 == 'TEXCOORD':
                            if 编号 == 0: 网格.顶点UV列表 = 列表
                        if 标识 == 'BLENDINDICES': 网格.骨骼ID索引值组列表 = 列表
                        if 标识 == 'BLENDWEIGHT': 网格.权重值组列表 = 列表
                        if 标识 == 'BONE_PALETTE': 网格.骨骼ID列表索引值列表 = 列表
                        if 标识 == 'MORPH_POSITION': 网格.形态键列表.append([标识, 编号, 列表])



    def 材质处理(self):
        for o in self.meshs:
            o.材质 = 接口.结构.插件材质()
            o.材质.名称 = o.材质名称
            o.材质.标签贴图相对地址列表 = self.__贴图处理__(o.贴图名称列表)


    def __贴图处理__(self, 贴图相对地址列表): # '106_03_D.dds', '106_03_N.dds'
        贴图标签列表 = []
        for 贴图地址 in 贴图相对地址列表:
            match 贴图地址[-5:-4]:
                case "d"|"D": 贴图标签 = "基础色"
                # case "s"|"S": 贴图标签 = "高光"
                case "n"|"N": 贴图标签 = "法向"
                # case "m"|"M": 贴图标签 = "糙度"
                case    _   : 贴图标签 = "其他"
            if "lightmap" in 贴图地址: 贴图标签 = "光照"
            贴图标签列表.append([贴图标签, f"..\\texture\\{贴图地址}"]) # 只能处理有在文件夹里的nif文件的贴图
        return 贴图标签列表


    def 表情处理(self):
        for o in self.meshs:
            for 网格 in o.网格列表:
                slidermin, slidermax = 0, 1
                形态键列表 = []
                if 网格.形态键列表 == []: continue
                标识, 编号, 基本顶点列表 = 网格.形态键列表[0]
                形态键列表.append(["morph_"+str(编号), slidermin, slidermax, 基本顶点列表])
                for [标识, 编号, 列表]in 网格.形态键列表[1:]:
                    形态顶点列表 = []
                    for [x0, y0, z0], [x1, y1, z1] in zip(基本顶点列表, 列表):
                        形态顶点列表.append( [x0+x1, y0+y1, z0+z1] )
                    形态键列表.append(["morph_"+str(编号), slidermin, slidermax, 形态顶点列表])
                网格.形态键列表 = 形态键列表


    def 权重处理(self, filedata):
        # 顶点index, [ [骨骼index, 权重值], [], []... ... ]
        # 顶点index, [ [骨骼名称 , 权重值], [], []... ... ]
        for o in self.meshs:
            for 网格 in o.网格列表:
                if "Face" in o.名称:
                    骨骼名称 = o.parent.名称
                    顶点个数 = len(网格.顶点列表)
                    网格.顶点骨骼组列表 = [[[骨骼名称, 1.0],] for i in range(顶点个数)]
                    continue

                if 网格.骨骼ID索引值组列表 == [] or 网格.权重值组列表 == [] or 网格.骨骼ID列表索引值列表 == []: continue


                for 权重值组, 骨骼ID索引值组 in zip(网格.权重值组列表, 网格.骨骼ID索引值组列表): # [0.83457, 0.16543002, 0.0], [9, 8, 0, 0]
                    骨骼组 = []
                    for 权重值, 骨骼ID索引值 in zip(权重值组, 骨骼ID索引值组):
                        骨骼IDindex = 网格.骨骼ID列表索引值列表[骨骼ID索引值]
                        骨骼ID = o.骨骼ID列表[骨骼IDindex]
                        骨骼名称 = filedata.datas[骨骼ID].名称
                        骨骼组.append( [骨骼名称, 权重值] )
                    网格.顶点骨骼组列表.append(骨骼组)



    def 网格处理(self):
        for o in self.meshs:
            for 网格 in o.网格列表:
                网格.顶点列表 = [o.matrix_local @ mathutils.Vector(position) for position in 网格.顶点列表]
                for i, [形态键名称, slidermin, slidermax, 顶点位置列表] in enumerate(网格.形态键列表):
                    新顶点位置列表 = [o.matrix_local @ mathutils.Vector(position) for position in 顶点位置列表]
                    网格.形态键列表[i][-1] = 新顶点位置列表


    def 模型处理(self):
        插件网格列表 = []
        for o in self.meshs:
            for i, 网格 in enumerate(o.网格列表):
                插件网格 = 接口.结构.插件网格()
                插件网格.名称 = o.名称 + "_" + str(i)
                插件网格.插件材质 = o.材质
                插件网格.顶点列表 = 网格.顶点列表
                插件网格.顶点UV列表 = 网格.顶点UV列表
                插件网格.顶点Loop列表 = 网格.顶点Loop列表
                插件网格.骨骼组列表 = 网格.顶点骨骼组列表
                插件网格.形态键列表 = 网格.形态键列表

                if 数据.变量.网格.导入缺UV网格 == False:
                    if 插件网格.顶点UV列表 == []: continue
                插件网格列表.append(插件网格)
        return 插件网格列表










