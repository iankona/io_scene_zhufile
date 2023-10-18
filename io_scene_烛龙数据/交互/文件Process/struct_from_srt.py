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
        self.材质列表 = self.材质处理(filedata)
        self.插件网格列表 = self.网格处理(filedata)
        # self.文件处理(filedata) 


    def 材质处理(self, filedata):
        材质列表 = []
        match filedata.head.magic:
            case "SRT 05.1.0": 材质列表 = self.__材质处理0500__(filedata)
            case "SRT 05.2.0": 材质列表 = self.__材质处理0500__(filedata)
            case "SRT 07.0.0": 材质列表 = self.__材质处理0700__(filedata)
        return 材质列表


    def __材质处理0500__(self, filedata):
        材质列表 = []
        for 材质名称, 贴图名称列表 in filedata.材质列表:
            材质 = 接口.结构.插件材质()
            材质.名称 = 材质名称
            材质.标签贴图相对地址列表 = self.__贴图处理0500__(贴图名称列表)
            材质列表.append(材质)
        return 材质列表

    def __贴图处理0500__(self, 贴图名称列表):
        贴图标签列表 = []
        for i, 贴图名称 in enumerate(贴图名称列表):
            match i:
                case 0: 贴图标签 = "基础色" # d
                case 1: 贴图标签 = "法向"   # n
                case 2: 贴图标签 = "高光"   # s
                case _: 贴图标签 = "其他"
            贴图标签列表.append([贴图标签, 贴图名称])
        return 贴图标签列表

    def __材质处理0700__(self, filedata):
        材质列表 = []
        for 材质名称, 贴图名称列表 in filedata.材质列表:
            材质 = 接口.结构.插件材质()
            材质.名称 = 材质名称
            材质.标签贴图相对地址列表 = self.__贴图处理0700__(贴图名称列表)
            材质列表.append(材质)
        return 材质列表


    def __贴图处理0700__(self, 贴图名称列表):
        贴图名称列表 = [贴图名称 for 贴图名称 in 贴图名称列表 if 贴图名称 != ""]
        贴图标签列表 = []
        for 贴图名称 in 贴图名称列表:
            match 贴图名称[-5:]:
                case "d.dds": 贴图标签 = "基础色" # d
                case "n.dds": 贴图标签 = "法向"   # n
                case "m.dds": 贴图标签 = "糙度"   # m
                case    _   : 贴图标签 = "其他"
            贴图标签列表.append([贴图标签, 贴图名称])
        return 贴图标签列表


    def 网格处理(self, filedata):
        网格列表 = []
        for 顶点列表, 顶点UV列表, 顶点Loop列表, 材质索引 in filedata.网格列表:
            插件网格 = 接口.结构.插件网格()
            插件网格.插件材质 = self.材质列表[材质索引]
            插件网格.顶点列表 = [mathutils.Vector(position) for position in 顶点列表]
            插件网格.顶点UV列表 = 顶点UV列表
            插件网格.顶点Loop列表 = 顶点Loop列表

            if 数据.变量.网格.导入缺UV网格 == False:
                if 插件网格.顶点UV列表 == []: continue  
            网格列表.append(插件网格)
        return 网格列表


    def 文件处理(self, filedata):
        for data in filedata.filelist: 类(data).struct_to_插件数据(数据.变量.选择集)











