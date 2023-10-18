import os
from ... import 数据

from .   import data_to_armatureobj
from .   import data_to_material
from .   import data_to_mesh
from .   import data_to_object


def 新建armatureobj():
    if 数据.变量.选择集.软件armatureobj != None: return None
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        if 插件数据.插件骨架 == None: continue
        armaturename = os.path.split(插件数据.filepath)[-1]
        armatureobj = data_to_armatureobj.新建骨架对象(armaturename, 插件数据.插件骨架)
        插件数据.软件armatureobj = armatureobj



def 新建material(): # 材质要求必须要有，贴图列表可以为[]
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for 插件网格 in 插件数据.插件网格列表:
            if 插件网格.插件材质.名称 in 数据.变量.选择集.材质字典:
                material = data_to_material.新建材质(数据.变量.选择集.材质字典[插件网格.插件材质.名称])
            else:
                material = data_to_material.新建材质(插件网格.插件材质)
            插件数据.软件materials.append(material)


def 新建mesh():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for 插件网格 in 插件数据.插件网格列表:
            meshname = 插件网格.名称
            if 插件网格.名称 == "": meshname = os.path.split(插件数据.filepath)[-1]
            mesh = data_to_mesh.新建网格(meshname, 插件网格)
            插件数据.软件meshs.append(mesh)


def 网格绑定材质():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for material, mesh in zip(插件数据.软件materials, 插件数据.软件meshs):
            mesh.materials.append(material)


def 新建object():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for mesh in 插件数据.软件meshs:
            object = data_to_object.新建模型(mesh)
            插件数据.软件objects.append(object)



def 模型绑定骨架():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for object in 插件数据.软件objects:
            armatureobj = 插件数据.软件armatureobj
            if 数据.变量.选择集.软件armatureobj is not None: armatureobj = 数据.变量.选择集.软件armatureobj
            if armatureobj == None: continue
            data_to_armatureobj.绑定骨架对象(object, armatureobj)


def 模型添加权重():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for object, 插件网格 in zip(插件数据.软件objects, 插件数据.插件网格列表):
            data_to_object.添加权重(object, 插件网格)


def 模型添加形态键():
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for object, 插件网格 in zip(插件数据.软件objects, 插件数据.插件网格列表):
            data_to_object.添加形态键(object, 插件网格)










