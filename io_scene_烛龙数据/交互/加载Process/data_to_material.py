import os
import bpy
from ... import 数据
from .   import shade




def 新建材质(插件材质):
    material = __选项__材质__(插件材质)
    check_existing = __选项__贴图__()
    location_context = __选项__节点位置布局__()
    __设置材质属性__(material, check_existing, location_context, 插件材质)
    __添加材质贴图__(material, check_existing, location_context, 插件材质)
    return material


def __选项__材质__(插件材质):
    if 数据.变量.材质.材质导入模式 == "引用现有材质" and 插件材质.名称 in bpy.data.materials:
        material = bpy.data.materials[插件材质.名称]
    else:
        material = __新建材质节点__(插件材质)
    return material

def __新建材质节点__(插件材质):
    material = bpy.data.materials.new(插件材质.名称)
    material.use_nodes = True
    # 开启Alpha效果
    material.blend_method = "CLIP"
    material.shadow_method = "CLIP"
    material.alpha_threshold = 0.1
    return material


def __选项__贴图__():
    if 数据.变量.材质.贴图导入模式 == "新建单独贴图":
        check_existing = False
    else:
        check_existing = True
    return check_existing


def __选项__节点位置布局__():
    x, y = 数据.变量.材质.x, 数据.变量.材质.y
    padx, pady = 数据.变量.材质.padx, 数据.变量.材质.pady
    rowsize, columnsize = 数据.变量.材质.rowsize, 数据.变量.材质.columnsize
    match 数据.变量.材质.材质节点布局:
        case "列表布局": location_context = shade.node_group_location_context_list.类(x=x, y=y, padx=padx, pady=pady)
        case "行高布局": location_context = shade.node_group_location_context_grid.类(x=x, y=y, padx=padx, pady=pady)
        case "网格布局": location_context = shade.node_group_location_context_mesh.类(x=x, y=y, rowsize=rowsize, columnsize=columnsize)
    return location_context



def __设置材质属性__(material, check_existing, location_context, 插件材质):
    for node in material.node_tree.nodes:
        if node.bl_idname == 'ShaderNodeOutputMaterial':
            node_output_material = node
            
        if node.bl_idname == 'ShaderNodeBsdfPrincipled':
            node_principled_bsdf = node

    location_context.add_node(node_output_material, row=0, column=0)
    location_context.add_node(node_principled_bsdf, row=0, column=1)

    node_output_material.label = "输出"
    node_principled_bsdf.label = "原理化BSDF"

    node_principled_bsdf.inputs["Base Color"].default_value = 插件材质.基础色
    node_principled_bsdf.inputs["Subsurface"].default_value = 插件材质.次表面
    node_principled_bsdf.inputs["Subsurface Radius"].default_value = 插件材质.次表面半径
    node_principled_bsdf.inputs["Subsurface Color"].default_value = 插件材质.次表面颜色
    node_principled_bsdf.inputs["Subsurface IOR"].default_value = 插件材质.次表面IOR
    node_principled_bsdf.inputs["Subsurface Anisotropy"].default_value = 插件材质.次表面各向异性
    node_principled_bsdf.inputs["Metallic"].default_value = 插件材质.金属度
    node_principled_bsdf.inputs["Specular"].default_value = 插件材质.高光
    node_principled_bsdf.inputs["Specular Tint"].default_value = 插件材质.高光染色
    node_principled_bsdf.inputs["Roughness"].default_value = 插件材质.糙度
    node_principled_bsdf.inputs["Anisotropic"].default_value = 插件材质.各向异性过滤
    node_principled_bsdf.inputs["Anisotropic Rotation"].default_value = 插件材质.各向异性旋转
    node_principled_bsdf.inputs["Sheen"].default_value = 插件材质.光泽
    node_principled_bsdf.inputs["Sheen Tint"].default_value = 插件材质.光泽染色
    node_principled_bsdf.inputs["Clearcoat"].default_value = 插件材质.清漆
    node_principled_bsdf.inputs["Clearcoat Roughness"].default_value = 插件材质.清漆粗糙度
    node_principled_bsdf.inputs["IOR"].default_value = 插件材质.IOR折射率
    node_principled_bsdf.inputs["Transmission"].default_value = 插件材质.透射
    node_principled_bsdf.inputs["Transmission Roughness"].default_value = 插件材质.透射粗糙度
    node_principled_bsdf.inputs["Emission"].default_value = 插件材质.自发光
    node_principled_bsdf.inputs["Emission Strength"].default_value = 插件材质.自发光强度
    node_principled_bsdf.inputs["Alpha"].default_value = 插件材质.透明


def __添加材质贴图__(material, check_existing, location_context, 插件材质):
    match 数据.变量.材质.法线导入模式:
        case "自动处理": __法线贴图__自动处理__(material, check_existing, location_context, 插件材质)
        case "手动设置": __法线贴图__手动设置__(material, check_existing, location_context, 插件材质)



def __法线贴图__自动处理__(material, check_existing, location_context, 插件材质):
    match os.path.splitext(插件材质.filepath)[-1]:
        case ".fbx"  : __法线贴图__自动处理__古剑1__(material, check_existing, location_context, 插件材质)
        case ".nif"  : __法线贴图__自动处理__古剑1__(material, check_existing, location_context, 插件材质)
        case ".xac"  : __法线贴图__自动处理__古剑1__(material, check_existing, location_context, 插件材质)
        case ".vmesh": __法线贴图__自动处理__古剑1__(material, check_existing, location_context, 插件材质)
        case ".model": __法线贴图__自动处理__古剑3__(material, check_existing, location_context, 插件材质)
        case ".srt"  : __法线贴图__自动处理__古剑1__(material, check_existing, location_context, 插件材质)
        case    _    : __法线贴图__自动处理__古剑1__(material, check_existing, location_context, 插件材质)


def __法线贴图__自动处理__古剑1__(material, check_existing, location_context, 插件材质):
    for node in material.node_tree.nodes:
        if node.bl_idname == 'ShaderNodeBsdfPrincipled': node_principled_bsdf = node

    for 贴图标签, 贴图路径 in 插件材质.标签贴图绝对地址列表:
        match 贴图标签:
            case "基础色"    : shade.material_node_group_default.添加_基础色贴图_伽玛值(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "次表面颜色": shade.material_node_group_default.添加_次表面颜色贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "高光"      : shade.material_node_group_default.添加_高光贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "糙度"      : shade.material_node_group_default.添加_糙度贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "法向"      : shade.material_node_group_default.添加_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径) 
            case "其他"      : shade.material_node_group_default.添加_其他贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)


def __法线贴图__自动处理__古剑3__(material, check_existing, location_context, 插件材质):
    for node in material.node_tree.nodes:
        if node.bl_idname == 'ShaderNodeBsdfPrincipled': node_principled_bsdf = node

    for 贴图标签, 贴图路径 in 插件材质.标签贴图绝对地址列表:
        match 贴图标签:
            case "基础色"    : shade.material_node_group_default.添加_基础色贴图_伽玛值(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "次表面颜色": shade.material_node_group_default.添加_次表面颜色贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "高光"      : shade.material_node_group_default.添加_高光贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "糙度"      : shade.material_node_group_normal_tangent.添加_古剑3_M贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "法向"      : shade.material_node_group_normal_tangent.添加_古剑3_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径) 
            case "其他"      : shade.material_node_group_default.添加_其他贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)


def __法线贴图__手动设置__(material, check_existing, location_context, 插件材质):
    for node in material.node_tree.nodes:
        if node.bl_idname == 'ShaderNodeBsdfPrincipled': node_principled_bsdf = node

    for 贴图标签, 贴图路径 in 插件材质.标签贴图绝对地址列表:
        match 贴图标签:
            case "基础色"    : shade.material_node_group_default.添加_基础色贴图_伽玛值(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "次表面颜色": shade.material_node_group_default.添加_次表面颜色贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "高光"      : shade.material_node_group_default.添加_高光贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "糙度"      : shade.material_node_group_default.添加_糙度贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "法向"      : __法线贴图__手动设置__法线空间__(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
            case "其他"      : shade.material_node_group_default.添加_其他贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)



def __法线贴图__手动设置__法线空间__(material, location_context, node_principled_bsdf, check_existing, 贴图路径):
    match 数据.变量.材质.法线贴图空间:
        case "切线空间"       : shade.material_node_group_normal_tangent.添加_古剑3_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
        case "物体空间"       : shade.material_node_group_normal_object.添加_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
        case "世界空间"       : shade.material_node_group_normal_world.添加_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
        case "Blender物体空间": shade.material_node_group_normal_blender_object.添加_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)
        case "Blender世界空间": shade.material_node_group_normal_blender_world.添加_法向贴图(material, location_context, node_principled_bsdf, check_existing, 贴图路径)