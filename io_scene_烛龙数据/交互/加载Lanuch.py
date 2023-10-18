
import os
import traceback

from .. import 数据, 接口, 工具
from .  import 路径Process
from .  import 文件Process, 加载Process
from .  import 变换Process, 骨架Process, 光影Process, 网格Process, 姿态Process


def 函数(directory, filegroups):  # 主逻辑
    选择集列表 = __主选择__(directory, filegroups)
    for 选择集 in 选择集列表 :  __主逻辑__(选择集)


# 注意，选择集名称需要手动设置
def __主选择__(directory, filegroups):
    选择集列表 = []
    filenames = [filegroup.name for filegroup in filegroups]
    filenames = [filename for filename in filenames if filename != ""] # E:\Program_StructFiles\GuJianQT2\characters\104\ ['']
    collection_filenames_list = 路径Process.路径Channel.查询古剑123filename字典(filenames)
    collection_filenames_dict = 路径Process.路径Channel.合并选择集列表(filenames, collection_filenames_list)
    选择集列表 = 路径Process.路径Channel.新建选择集列表(directory, collection_filenames_dict)
    return 选择集列表


def __主逻辑__(选择集):
    # 设置变量
    数据.变量.选择集 = 选择集
    # 解析文件
    文件Process.path_to_data_to_struct_to_插件数据.函数()
    # 处理
    __骨架Channel__() # 默认 object 都挂载在 bpy.context.scene.collection 
    加载Process.择集Process.合并与略过骨架()
    加载Process.择集Process.左右手指长度一致()
    加载Process.择集Process.新建armatureobj() # 默认 object 都挂载在 bpy.context.scene.collection 

    __模型Channel__() # 默认 object 都挂载在 bpy.context.scene.collection 
    加载Process.择集Process.文件骨架新建T姿势action()


    加载Process.择集Process.合并文件姿态()
    __动画Channel__()
    
    加载Process.择集Process.新建collection() 
    加载Process.择集Process.move_objects_from_collection_to_collection() # 从 bpy.context.scene.collection 中移动 object
    加载Process.择集Process.古剑1新建Break子选择集and移动Objects() # 包含从 bpy.context.scene.collection 中移动 object
    __递归选择集Channel__()
    

def __骨架Channel__():
    骨架Process.文件Local空间2BlenderEditBone空间.文件骨架_Matrix_Local_Decompose()
    变换Process.坐标Process.骨架Process()
    变换Process.旋转Process.骨架Process()
    变换Process.缩放Process.骨架Process()
    骨架Process.文件Local空间2BlenderEditBone空间.插件数据_转换处理()
    骨架Process.编辑Process.骨骼长度处理()
    


def __模型Channel__():
    光影Process.UVProcess.UV处理()
    光影Process.贴图Process.贴图处理()

    变换Process.坐标Process.网格Process()
    变换Process.旋转Process.网格Process()
    变换Process.缩放Process.网格Process()
    网格Process.权重Process.顶点索引骨骼组列表2骨骼名称顶点组字典()
    
    加载Process.模型Process.新建material()
    加载Process.模型Process.新建mesh()
    加载Process.模型Process.网格绑定材质()
    加载Process.模型Process.新建object()
    加载Process.模型Process.新建armatureobj()
    加载Process.模型Process.模型绑定骨架()
    加载Process.模型Process.模型添加权重()
    加载Process.模型Process.模型添加形态键()

    
def __动画Channel__():
    变换Process.坐标Process.姿态Process()
    变换Process.缩放Process.姿态Process()
    姿态Process.择架Process.find_blender_armatures()
    姿态Process.文件Bone空间2BlenderBasis空间.预处理姿态()
    姿态Process.文件Bone空间2BlenderBasis空间.Auto姿态_to_Basis姿态()
    姿态Process.通道Process.通道坐标系变换_各自处理()
    # # 加载
    加载Process.姿态Process.新建action()


def __递归选择集Channel__():
    # 递归, 加载
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for 文件选择集 in 插件数据.选择集列表: __主逻辑__(文件选择集)