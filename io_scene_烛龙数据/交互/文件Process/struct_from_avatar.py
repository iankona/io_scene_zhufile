

import os
from . import struct
from ... import 数据, 接口, 工具, 交互
# from .. import 路径Process

class 类(struct.struct):
    def __init__(self, filedata):
        struct.struct.__init__(self) 
        self.filepath = filedata.filepath      
        self.__材质字典__ = self.材质处理(filedata)
        self.选择集列表 = self.文件路径处理(filedata)


    def 材质处理(self, filedata): # <g3_eye>_left
        材质字典 = {}
        for mnode in filedata.材质节点列表:
            插件材质 = 接口.结构.插件材质()
            插件材质.名称 = mnode.name
            插件材质.标签贴图绝对地址列表 = self.__贴图处理__(filedata, mnode)
            材质字典[mnode.name] = 插件材质
        return 材质字典


    def __贴图处理__(self, filedata, mnode): 
        dirname = os.path.dirname(os.path.dirname(filedata.filepath))
        贴图标签列表 = []
        if mnode.TexBaseIris != None:   贴图标签列表.append(["基础色", dirname+"\\"+mnode.TexBaseIris])
        if mnode.TexBaseSclera != None: 贴图标签列表.append(["次表面颜色", dirname+"\\"+mnode.TexBaseSclera])
        if 数据.变量.古剑3选项.眼睛开启高光: 
            高光贴图路径 = self.__高光贴图路径__(filedata)
            if 高光贴图路径 != None:    贴图标签列表.append(["高光", 高光贴图路径])
        if mnode.TexAOMask != None:     贴图标签列表.append(["其他", dirname+"\\"+mnode.TexAOMask])
        return 贴图标签列表
    

    def 文件路径处理(self, filedata):
        dirname = os.path.dirname(os.path.dirname(filedata.filepath))
        filepaths = []
        for anode in filedata.路径节点列表:
            if anode.type == "skin" and anode.file != None: filepaths.append(dirname+"\\"+anode.file)

        选择集 = 接口.标记.选择集()
        选择集.名称 = self.__查询__古剑3字典__(filedata.filepath)
        选择集.filepaths = filepaths
        选择集.材质字典 = self.__材质字典__
        return [选择集]


    def __高光贴图路径__(self, filedata):
        # "E:\Program_StructFiles\GuJianQT3\asset\avatar\actress1_coat.avatar"
        # materials/textures/eye/eye_iris_004.dds
        # materials\textures\eye\eye_sclera_001.dds
        # materials\textures\eye\T_FemaleEyeAOMask.dds
        # <skin file="characters/actress1/models/actress1_morphface.model" tag="morphface">
        # "E:\Program_StructFiles\GuJianQT3\asset\characters\actress1\textures\actress1_eye_00d.dds"
        character_name = None # actress1
        morphface_path = None
        for anode in filedata.路径节点列表:
            if anode.tag == "morphface" and anode.file != None: 
                morphface_path = anode.file # "characters/actress1/models/actress1_morphface.model"
                character_name = os.path.basename(morphface_path).split("_")[0]

        贴图路径 = None
        if character_name != None:
            assetdir = os.path.dirname(os.path.dirname(filedata.filepath))
            贴图路径 = assetdir + "\\characters\\" + character_name + "\\textures\\" + character_name +  "_eye_00d.dds"
        return 贴图路径

    def __查询__古剑3字典__(self, filepath):
        # ".avatar"
        filename = os.path.basename(filepath)
        if "古剑3" not in 数据.变量.选择.名称替换: return filename
        if filename in 数据.常量.古剑3字典: filename = 数据.常量.古剑3字典[filename]
        # 路径Process.路径Channel.recent_collection_name = filename # 古剑3的角色、模型及动画都是分开的，本身就只能分开处理
        return filename