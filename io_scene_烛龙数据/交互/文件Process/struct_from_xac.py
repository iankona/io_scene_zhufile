

import os
import bpy
import mathutils
from . import struct
from ... import 数据, 接口, 工具
from .   import 列表补齐



class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath       
        self.文件骨架 = self.骨架处理(filedata)
        self.插件材质列表 = self.材质处理(filedata)
        self.插件网格列表 = self.模型处理(filedata)
        self.文件处理(filedata)


    def 骨架处理(self, filedata):
        文件骨架 = 接口.结构.文件骨架()
        for position, [qx, qy, qz, qw], scale, parentid, bonename in filedata.LEKS.骨骼节点列表:
            文件骨骼 = 文件骨架.骨骼()
            文件骨骼.name = bonename
            文件骨骼.parentname = filedata.LEKS.骨骼节点列表[parentid][-1] if parentid != -1 else ""
            文件骨骼.matrix_local = mathutils.Matrix.LocRotScale(mathutils.Vector(position), mathutils.Quaternion([qw, qx, qy, qz]), mathutils.Vector(scale))
            if 文件骨骼.parentname != "":
                文件骨骼.matrix_local = 文件骨架.骨骼字典[文件骨骼.parentname].matrix_local @ 文件骨骼.matrix_local

            文件骨架.骨骼字典[bonename] = 文件骨骼
        return 文件骨架


    def 材质处理(self, filedata):
        插件材质列表 = []
        for 材质名称, 材质属性列表, 贴图基本名称列表, 贴图属性列表 in filedata.lrtmlist:
            插件材质 = 接口.结构.插件材质()
            插件材质.名称 = 材质名称
            插件材质.标签贴图相对地址列表 = self.__贴图处理__(贴图基本名称列表)
            插件材质列表.append(插件材质)
        return 插件材质列表



    def 模型处理(self, filedata): # 除了古剑1 有网格名称，其他文件基本没有网格名称
        文件插件网格列表 = []
        for HSMV, THGW, STCM in zip(*列表补齐.函数(filedata.hsmvlist, filedata.thgwlist, filedata.stcmlist)) :
            形态键列表 = []
            顶点骨骼组列表 = []
            # 模型插件网格列表 = []
            if HSMV is None: continue
            if STCM is not None:
                try:
                    形态键列表 = self.__表情处理__(HSMV, STCM)
                except:
                    pass # 需解决索引超出范围，也许表情块存在索引的HSMV指向
            if THGW is not None:
                try:
                    顶点骨骼组列表 = self.__权重处理__(HSMV, THGW, filedata.LEKS)
                except:
                    pass # 也许有指针，不确定
            # 模型插件网格列表 = self.__网格处理__(HSMV, 形态键列表, 顶点骨骼组列表)
            文件插件网格列表 += self.__网格处理__(HSMV, 形态键列表, 顶点骨骼组列表)
        return 文件插件网格列表


    def 文件处理(self, filedata):
        for data in filedata.filelist: 类(data).struct_to_插件数据(数据.变量.选择集)


    def __网格处理__(self, HSMV, 形态键列表, 顶点骨骼组列表):
        插件网格列表 = []
        start = 0
        for j, [顶点个数, Loop个数, 材质索引, 顶点Loop列表, 骨骼个数, 骨骼映射列表] in enumerate(HSMV.顶点划分信息列表):
            插件网格 = 接口.结构.插件网格()
            插件网格.插件材质 = self.插件材质列表[材质索引]
            插件网格.顶点列表 = [mathutils.Vector(position) for position in HSMV.顶点列表[start: start+顶点个数]]
            插件网格.顶点UV列表 = HSMV.顶点UV列表[start: start+顶点个数]
            插件网格.顶点Loop列表 = 顶点Loop列表

            if 形态键列表 != []:
                for 形态键名称, slidermin, slidermax, 新顶点列表 in 形态键列表:
                    形态顶点列表 = [mathutils.Vector(position) for position in 新顶点列表[start: start+顶点个数]]
                    插件网格.形态键列表.append( [ 形态键名称, slidermin, slidermax, 形态顶点列表] )

            if 顶点骨骼组列表 != []:
                插件网格.骨骼组列表 = 顶点骨骼组列表[start: start+顶点个数]

            start += 顶点个数

            if 数据.变量.网格.导入缺UV网格 == False:
                if 插件网格.顶点UV列表 == []: continue
            插件网格列表.append(插件网格)
        return 插件网格列表


    def __表情处理__(self, HSMV, STCM):
        slidermin, slidermax = 0, 1
        形态键列表 = []
        形态键列表.append(["basic", slidermin, slidermax, HSMV.顶点列表[:]])
        for [形态键名称, positionoffset, positionindex] in STCM.形态键列表:
            新顶点列表 = HSMV.顶点列表[:]
            for index, offset in zip(positionindex, positionoffset):
                x0, y0, z0 = 新顶点列表[index]
                x1, y1, z1 = offset
                新顶点列表[index] = [x0+x1, y0+y1, z0+z1]
            形态键列表.append( [形态键名称, slidermin, slidermax, 新顶点列表] )
        return 形态键列表

    def __权重处理__(self, HSMV, THGW, LEKS):
        # 顶点index, [ [骨骼index, 权重值], [], []... ... ]
        # 顶点index, [ [骨骼名称 , 权重值], [], []... ... ]
        权重组列表 = []
        for 索引左值, 权重个数 in THGW.区权重信息列表:
            权重组列表.append(THGW.权重值Loop列表[索引左值: 索引左值+权重个数])

        顶点骨骼组列表 = []
        for index in HSMV.区权重索引Loop列表:
            顶点骨骼组列表.append(权重组列表[index][:])  # 注意引用和复制的区别

        for 权重组 in 顶点骨骼组列表:
            for i, [权重值, 骨骼ID] in enumerate(权重组):
                骨骼名称 = LEKS.骨骼节点列表[骨骼ID][-1]
                权重组[i] = [骨骼名称, 权重值]
        return 顶点骨骼组列表


    def __贴图处理__(self, 贴图基本名称列表): # 104_body_d, 104_body_n
        去重贴图基本名称列表 = []
        for 贴图基本名称 in 贴图基本名称列表:
            if 贴图基本名称 not in 去重贴图基本名称列表: 去重贴图基本名称列表.append(贴图基本名称)

        贴图相对地址列表 = [char+".dds" for char in 去重贴图基本名称列表]

        贴图标签列表 = []
        for 贴图地址 in 贴图相对地址列表:
            match 贴图地址[-5:-4]:
                case "d": 贴图标签 = "基础色"
                case "s": 贴图标签 = "高光"
                case "n": 贴图标签 = "法向"
                # case "m": 贴图标签 = "糙度"
                case  _ : 贴图标签 = "其他"
            贴图标签列表.append([贴图标签, 贴图地址])
        return 贴图标签列表
    
