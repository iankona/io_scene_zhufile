import os
import bpy



def 添加_基础色贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    location_context.add_node(node_texture_image, row=0, column=6)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_principled_bsdf.inputs["Base Color"])
    material.node_tree.links.new(node_texture_image.outputs["Alpha"], node_principled_bsdf.inputs["Alpha"])



def 添加_基础色贴图_伽玛值(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    location_context.add_node(node_texture_image, row=0, column=6)

    node_texture_gamma = material.node_tree.nodes.new(type='ShaderNodeGamma')
    node_texture_gamma.inputs[1].default_value = 1
    location_context.add_node(node_texture_gamma, row=0, column=2)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_texture_gamma.inputs["Color"])
    material.node_tree.links.new(node_texture_gamma.outputs["Color"], node_principled_bsdf.inputs["Base Color"])
    material.node_tree.links.new(node_texture_image.outputs["Alpha"], node_principled_bsdf.inputs["Alpha"])



def 添加_次表面颜色贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    location_context.add_node(node_texture_image, row=1, column=6)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_principled_bsdf.inputs["Subsurface Color"])


def 添加_高光贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=2, column=6)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_principled_bsdf.inputs["Specular"])


def 添加_高光贴图_反转(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=2, column=6)

    node_texture_invert = material.node_tree.nodes.new(type='ShaderNodeInvert')
    location_context.add_node(node_texture_invert, row=2, column=2)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_texture_invert.inputs["Color"])
    material.node_tree.links.new(node_texture_invert.outputs["Color"], node_principled_bsdf.inputs["Specular"])



def 添加_糙度贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=3, column=6)

    node_texture_invert = material.node_tree.nodes.new(type='ShaderNodeInvert')
    location_context.add_node(node_texture_invert, row=3, column=2)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_texture_invert.inputs["Color"])
    material.node_tree.links.new(node_texture_invert.outputs["Color"], node_principled_bsdf.inputs["Roughness"])

def 添加_糙度贴图_反转(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=3, column=6)

    node_texture_invert = material.node_tree.nodes.new(type='ShaderNodeInvert')
    location_context.add_node(node_texture_invert, row=3, column=2)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_texture_invert.inputs["Color"])
    material.node_tree.links.new(node_texture_invert.outputs["Color"], node_principled_bsdf.inputs["Roughness"])


def 添加_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=4, column=6)

    node_normalmap = material.node_tree.nodes.new(type='ShaderNodeNormalMap')
    node_normalmap.space = 'BLENDER_OBJECT'
    location_context.add_node(node_normalmap, row=4, column=2)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_normalmap.inputs["Color"])
    material.node_tree.links.new(node_normalmap.outputs["Normal"], node_principled_bsdf.inputs["Normal"])


count = 5
def 添加_其他贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    global count 
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=count, column=7)
    count += 1

