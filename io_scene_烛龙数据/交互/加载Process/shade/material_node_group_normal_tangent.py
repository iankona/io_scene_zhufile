

import os
import bpy


# 贴图 -> 分离rgb
# r -> 金属
# g -> 光泽
# g -> 反转 -> 粗糙
# b -> AO
def 添加_古剑3_M贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=3, column=6)


    node_separate_rgb = material.node_tree.nodes.new(type='ShaderNodeSeparateRGB') # 分离rgb
    location_context.add_node(node_separate_rgb, row=3, column=5)


    node_invert_g = material.node_tree.nodes.new(type='ShaderNodeInvert')
    location_context.add_node(node_invert_g, row=3, column=4)


    # node_combine_rgb = material.node_tree.nodes.new(type='ShaderNodeCombineRGB') # 合并rgb
    # location_context.add_node(node_combine_rgb, row=3, column=3)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_separate_rgb.inputs["Image"])
    # material.node_tree.links.new(node_separate_rgb.outputs["R"], node_principled_bsdf.inputs["Metallic"]) # 金属度

    # material.node_tree.links.new(node_separate_rgb.outputs["G"], node_principled_bsdf.inputs["Sheen"]) # 光泽

    material.node_tree.links.new(node_separate_rgb.outputs["G"], node_invert_g.inputs["Color"]) 
    material.node_tree.links.new(node_invert_g.outputs["Color"], node_principled_bsdf.inputs["Roughness"]) # 粗糙

    # material.node_tree.links.new(node_separate_rgb.outputs["B"], node_principled_bsdf.inputs["Transmission"]) # 透射
 

# 贴图 -> 分离rgb
# r -> 合并rgb
# g -> 反转 -> 合并rgb
# b -> 反转 -> 合并rgb
# 合并rgb -> normal.tangent
def 添加_古剑3_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    if os.path.exists(贴图路径) == False: return ""
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    location_context.add_node(node_texture_image, row=4, column=6)

    node_separate_rgb = material.node_tree.nodes.new(type='ShaderNodeSeparateRGB') # 分离rgb
    location_context.add_node(node_separate_rgb, row=4, column=5)

    node_invert_g = material.node_tree.nodes.new(type='ShaderNodeInvert')
    location_context.add_node(node_invert_g, row=5, column=4)

    node_invert_b = material.node_tree.nodes.new(type='ShaderNodeInvert')
    location_context.add_node(node_invert_b, row=6, column=4)

    node_combine_rgb = material.node_tree.nodes.new(type='ShaderNodeCombineRGB') # 合并rgb
    location_context.add_node(node_combine_rgb, row=4, column=3)

    node_normalmap = material.node_tree.nodes.new(type='ShaderNodeNormalMap')
    node_normalmap.space = 'TANGENT'
    location_context.add_node(node_normalmap, row=4, column=2)

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_separate_rgb.inputs["Image"])

    material.node_tree.links.new(node_separate_rgb.outputs["R"], node_combine_rgb.inputs["R"]) 
    material.node_tree.links.new(node_separate_rgb.outputs["G"], node_invert_g.inputs["Color"]) 
    material.node_tree.links.new(node_invert_g.outputs["Color"], node_combine_rgb.inputs["G"]) 
    material.node_tree.links.new(node_separate_rgb.outputs["B"], node_invert_b.inputs["Color"]) 
    material.node_tree.links.new(node_invert_b.outputs["Color"], node_combine_rgb.inputs["B"]) 

    material.node_tree.links.new(node_combine_rgb.outputs["Image"], node_normalmap.inputs["Color"])
    material.node_tree.links.new(node_normalmap.outputs["Normal"], node_principled_bsdf.inputs["Normal"])