import os
import bpy
from ... import 数据


def 新建骨架对象(名称, 插件骨架):
    armatureobj = bpy.data.objects.new(名称, bpy.data.armatures.new(名称))
    bpy.context.scene.collection.objects.link(armatureobj)
    
    bpy.context.view_layer.objects.active = armatureobj # 要求上一行，必须存在，Error: ViewLayer 'ViewLayer' does not contain object 'm04-1.nif'
    bpy.ops.object.mode_set(mode = 'EDIT')
    for name, databone in 插件骨架.骨骼字典.items():
        ebone = armatureobj.data.edit_bones.new(name)
        ebone.head = databone.head
        ebone.tail = databone.tail
        ebone.roll = databone.roll
        ebone.length = databone.length

        if databone.parent is not None: ebone.parent = armatureobj.data.edit_bones[databone.parent.name]
    bpy.ops.object.mode_set(mode = 'OBJECT')

    return armatureobj


def 绑定骨架对象(object, armatureobj):
    object.parent = armatureobj
    骨架修改器 = object.modifiers.new(armatureobj.name, 'ARMATURE')
    骨架修改器.object = armatureobj


