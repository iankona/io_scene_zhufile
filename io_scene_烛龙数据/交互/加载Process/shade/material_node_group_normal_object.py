import os
import bpy



def 添加_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=4, column=3)

    node_normalmap = material.node_tree.nodes.new(type='ShaderNodeNormalMap')
    node_normalmap.space = 'OBJECT'
    location_context.add_node(node_normalmap, row=4, column=2)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_normalmap.inputs["Color"])
    material.node_tree.links.new(node_normalmap.outputs["Normal"], node_principled_bsdf.inputs["Normal"])
