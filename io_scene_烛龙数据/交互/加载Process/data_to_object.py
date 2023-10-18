import os
import bpy

from ... import 数据




def 新建模型(mesh):
    object = bpy.data.objects.new(mesh.name, mesh)
    bpy.context.scene.collection.objects.link(object)
    return object


def 添加权重(object, 插件网格):
    for 骨骼名称, 顶点组 in 插件网格.顶点组字典.items():
        vertex_group = object.vertex_groups.new(name=骨骼名称)
        for 顶点index, 权重值 in 顶点组: vertex_group.add( [顶点index], 权重值, "ADD" )


def 添加形态键(object, 插件网格):
    for 形态键名称, slidermin, slidermax, 顶点位置列表 in 插件网格.形态键列表:
        shape_key = object.shape_key_add(name = 形态键名称)  # bpy.data.shape_keys['Key'].key_blocks["MORPH_POSITION_0"]
        shape_key.slider_min = slidermin
        shape_key.slider_max = slidermax
        for location, vertice in zip(顶点位置列表, shape_key.data): vertice.co = location