# https://github.com/CucFlavius/Zee-010-Templates/blob/main/HKSplineCompressedAnimation.bt
# https://github.com/CucFlavius/Zee-010-Templates/blob/main/FFXIV_PAP.bt_bak
# https://github.com/Meowmaritus/SoulsAssetPipeline/blob/master/SoulsAssetPipeline/Animation/HKX/SplineCompressedAnimation.cs

import os
import mathutils
from . import struct
from ... import 数据, 接口, 工具


class 类:
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath  
        self.插件材质列表 = self.材质处理(filedata)
        self.插件网格列表 = self.模型处理(filedata)


    def 材质处理(self, filedata):
        插件材质列表 = []
        for lrtm in filedata.SRTM.材质列表:
            插件材质 = 接口.结构.插件材质()
            插件材质.名称 = lrtm.材质名称 # Material #49/<g3_cloth2>actress2_bx_body , 'Material #6388/<cloth><g3_cloth2>actress1_md_body'
            插件材质.标签贴图相对地址列表 = self.__texture__filepath__(lrtm.相对贴图地址列表)
            插件材质列表.append(插件材质)
        return 插件材质列表


    def 模型处理(self, filedata):
        插件网格列表 = []
        for i, [loop左值, loop个数, vert左值, vert个数, 材质索引] in enumerate(filedata.MBUS.顶点划分信息列表) :
            插件网格 = 接口.结构.插件网格()
            插件网格.材质 = self.插件材质列表[材质索引]
            插件网格.顶点列表 = [mathutils.Vector(position) for position in filedata.HSMV.mesh.顶点列表[vert左值: vert左值+vert个数]]
            插件网格.顶点UV列表 = filedata.HSMV.mesh.顶点UV列表[vert左值: vert左值+vert个数]
            插件网格.顶点Loop列表 = [ loop个值-vert左值 for loop个值 in filedata.HSMV.mesh.顶点Loop列表[loop左值: loop左值+loop个数] ]
            
            if 数据.变量.网格.导入缺UV网格 == False:
                if 插件网格.顶点UV列表 == []: continue  
            插件网格列表.append(插件网格)
        return 插件网格列表


    def __texture__filepath__(self, 贴图相对地址列表): # ['..\\textures\\actress1_md_body_01d.tga', '..\\textures\\actress1_md_body_01s.tga', '..\\textures\\actress1_md_body_01n.tga', '..\\textures\\actress1_md_body_01m.tga']
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








