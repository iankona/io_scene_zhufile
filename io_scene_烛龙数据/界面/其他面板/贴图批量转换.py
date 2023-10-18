import os

import bpy

from ... import 工具


# blender 中如何给 bpy.types.Operator 传值
# use https://blog.csdn.net/WPAPA/article/details/120704431 as a reference

class ZHUFILE_PROP_DDS组(bpy.types.PropertyGroup):
    Layer: bpy.props.EnumProperty(
        items = (
            ("Layer_0", "Layer_0", ""),
            ),
        default='Layer_0',
        )


class ZHUFILE_PROP_PNG组(bpy.types.PropertyGroup):
    Layer: bpy.props.EnumProperty(
        items = (
            ("Layer_0", "Layer_0", ""),
            ),
        default='Layer_0',
        )

    Mipmap: bpy.props.EnumProperty(
        items = (
            ("Mipmap_0",  "Mipmap_0",  ""),
            ("Mipmap_1",  "Mipmap_1",  ""),
            ("Mipmap_2",  "Mipmap_2",  ""),
            ("Mipmap_3",  "Mipmap_3",  ""),
            ("Mipmap_4",  "Mipmap_4",  ""),
            ("Mipmap_5",  "Mipmap_5",  ""),
            ("Mipmap_6",  "Mipmap_6",  ""),
            ("Mipmap_7",  "Mipmap_7",  ""),
            ("Mipmap_8",  "Mipmap_8",  ""),
            ("Mipmap_9",  "Mipmap_9",  ""),
            ("Mipmap_10", "Mipmap_10", ""),
            ("Mipmap_11", "Mipmap_11", ""),
            ("Mipmap_12", "Mipmap_12", ""),
            ),
        default = 'Mipmap_0',
        )

    Data_Type: bpy.props.EnumProperty(
        items = (
            ("UNORM", "UNORM", ""),
            ("SRGB",  "SRGB",  ""),
            ),
        default = 'UNORM',
        )

    UNORM_Format: bpy.props.EnumProperty(
        items = (
            ("R8_UNORM",     "R8_UNORM",     ""),
            ("RA8_UNORM",    "RA8_UNORM",    ""),
            ("RGB8_UNORM",   "RGB8_UNORM",   ""),
            ("RGBA8_UNORM",  "RGBA8_UNORM",  ""),
            ("R16_UNORM",    "R16_UNORM",    ""),
            ("RA16_UNORM",   "RA16_UNORM",   ""),
            ("RGB16_UNORM",  "RGB16_UNORM",  ""),
            ("RGBA16_UNORM", "RGBA16_UNORM", ""),
            ),
        default = 'RGBA8_UNORM',
        )

    SRGB_Format: bpy.props.EnumProperty(
        items = (
            ("R8_SRGB",    "R8_SRGB",    ""),
            ("RA8_SRGB",   "RA8_SRGB",   ""),
            ("RGB8_SRGB",  "RGB8_SRGB",  ""),
            ("RGBA8_SRGB", "RGBA8_SRGB", ""),
            ),
        default = 'RGBA8_SRGB',
        )
    

class ZHUFILE_PROP_文件(bpy.types.PropertyGroup): 
    """用于列表中单个项目的属性组"""

    name: bpy.props.StringProperty(
        name="name",
        description="文件名称",
        default="未命名")

    path: bpy.props.StringProperty(
        name="path",
        description="文件路径",
        default="")

    prop: bpy.props.StringProperty(
        name="prop",
        description="其他属性",
        default="")


class ZHUFILE_UL_选择文件列表(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        custom_icon = 'OBJECT_DATAMODE'
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon=custom_icon)

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon=custom_icon)


class ZHUFILE_UL_保存文件列表(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        custom_icon = 'OBJECT_DATAMODE'
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon=custom_icon)

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon=custom_icon)





# # operator = None
# # png = None
# class ZHUFILE_OT_贴图_批量转换_挂载实例(bpy.types.Operator):
#     bl_idname = "zhufile.instance_texture_batch_convert" # -> ZHUFILE_OT_property_texture_batch_convert
#     bl_label  = "挂载实例" 

#     # # 不能用下面的方式，会遇到
#     # # TypeError: UILayout.prop(): error with argument 1, "data" -  Function.data expected a AnyType type, not _PropertyDeferred
#     # # <_PropertyDeferred, <built-in function PointerProperty>, {'type': <class 'io_scene_烛龙数据.界面.其他面板.贴图批量转换.ZHUFILE_PROP_PNG组'>}>
#     # dds = bpy.props.PointerProperty(type=ZHUFILE_PROP_DDS组)
#     # png = bpy.props.PointerProperty(type=ZHUFILE_PROP_PNG组)
#     # 选择集索引 = bpy.props.IntProperty(name="选择集索引", default=0)
#     # 选择集文件 = bpy.props.CollectionProperty(type=ZHUFILE_PROP_选择文件)
#     # 保存集索引 = bpy.props.IntProperty(name="保存集索引", default=0)
#     # 保存集文件 = bpy.props.CollectionProperty(type=ZHUFILE_PROP_保存文件)

#     # 不能用下面的方式，每次调用draw()函数，都会新建类和销毁类，导致每次draw()，png都是不同内存地址，表现上就是属性修改不起作用
#     # dds: bpy.props.PointerProperty(type=ZHUFILE_PROP_DDS组)
#     # png: bpy.props.PointerProperty(type=ZHUFILE_PROP_PNG组)
#     # 选择集索引: bpy.props.IntProperty(name="选择集索引", default=0)
#     # 选择集文件: bpy.props.CollectionProperty(type=ZHUFILE_PROP_选择文件)
#     # 保存集索引: bpy.props.IntProperty(name="保存集索引", default=0)
#     # 保存集文件: bpy.props.CollectionProperty(type=ZHUFILE_PROP_保存文件)
#     def execute(self, context):
#         # print("函数有执行", png, bpy.types.ZHUFILE_OT_instance_texture_batch_convert.png)
#         return {'FINISHED'}
#     def draw(self, context):
#         pass
#     def invoke(self, context, event):
#         # context.window_manager.invoke_props_dialog(self)
#         return  {'RUNNING_MODAL'}



class ZHUFILE_OT_贴图_批量转换_添加函数(bpy.types.Operator):
    bl_idname = "zhufile.func_add_texture_batch_convert"
    bl_label  = "添加函数" 
    # print(bpy.context.space_data.params.files) # AttributeError: 'FileSelectParams' object has no attribute 'files'
    # operator: bpy.props.PointerProperty(type=bpy.types.PropertyGroup) # AttributeError: bpy_struct: attribute "operator" from "ZHUFILE_OT_func_add_texture_batch_convert" is read-only
    def execute(self, context):
        __添加函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}

def __添加函数__():
    if bpy.context.space_data.type != 'FILE_BROWSER' or bpy.context.space_data.browse_mode != 'FILES': return None
    operator = bpy.context.space_data.operator
    directory = operator.directory
    filegroups = operator.files
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    for filegroup in filegroups:
        filepath = directory + filegroup.name
        is_in_group = False
        for fileprop in addon_prefs.选择文件组:
            if fileprop.path == filepath:
                is_in_group = True
                break
        if is_in_group: continue
        fileprop = addon_prefs.选择文件组.add()
        fileprop.name = filegroup.name
        fileprop.path = filepath


class ZHUFILE_OT_贴图_批量转换_转换函数(bpy.types.Operator):
    bl_idname = "zhufile.func_run_texture_batch_convert"
    bl_label  = "转换函数" 
    def execute(self, context):
        __转换函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)

def __转换函数__():
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    indexlayer = int(addon_prefs.png.Layer.split("_")[-1])
    indexmipmap = int(addon_prefs.png.Mipmap.split("_")[-1])
    match addon_prefs.png.Data_Type:
        case "SRGB": datatype = addon_prefs.png.SRGB_Format
        case "UNORM": datatype = addon_prefs.png.UNORM_Format
    filepaths = [fileprop.path for fileprop in addon_prefs.选择文件组]
    ddsfilepaths = [filepath for filepath in filepaths if filepath.endswith(".dds")]
    for ddsfilepath in ddsfilepaths:
        pngfilepath = 工具.format_convert.dds_convert_to_png(ddsfilepath, indexlayer, indexmipmap, datatype)
        is_in_group = False
        for fileprop in addon_prefs.保存文件组:
            if fileprop.path == pngfilepath:
                is_in_group = True
                break
        if is_in_group: continue
        fileprop = addon_prefs.保存文件组.add()
        fileprop.name = os.path.basename(pngfilepath)
        fileprop.path = pngfilepath


class ZHUFILE_OT_贴图_批量转换_清空函数(bpy.types.Operator):
    bl_idname = "zhufile.func_clear_texture_batch_convert"
    bl_label  = "清空函数" 
    def execute(self, context):
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.选择文件组.clear()
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.保存文件组.clear()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)




class ZHUFILE_OT_贴图_批量转换_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_texture_batch_convert" # -> ZHUFILE_OT_property_texture_batch_convert
    bl_label  = "选项设置" 

    def execute(self, context):
        # print("OK有运行")
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.选择文件组.clear()
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.保存文件组.clear()
        return {'FINISHED'}
    def draw(self, context):
        draw(self)
        
    def invoke(self, context, event):
        context.window_manager.invoke_props_dialog(self, width=500)
        return {'RUNNING_MODAL'}



class ZHUFILE_PT_贴图_批量转换_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_texture_batch_convert_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "贴图批量转换.选项设置" # 不能删除
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 25

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import"

    def draw(self, context):
        draw(self)
        # operator = layout.operator("ZHUFILE_OT_property_texture_batch_convert", text="贴图批量转换弹窗") # <bpy_struct, ZHUFILE_OT_property_texture_batch_convert at 0x000002D376A62FC8>
        # operator = bpy.ops.zhufile.property_texture_batch_convert # <function bpy.ops.zhufile.property_texture_batch_convert at 0x1d5a962acb0'>

def draw(self):
    layout = self.layout
    layout.label(text="请使用 Ctrl+鼠标点击 进行多选...")
    layout.label(text="若使用 Shift+鼠标点击 进行多选，需右键1次，才能生效...")
    layout.label(text="右键会弹出菜单，不用理会，鼠标移动到右侧面板点击即可...")
    # layout.label(text="-------------------------------------------------------")
    layout.separator() # 在项目之间的布局中插入空白空间
    # layout.separator_spacer() # 在项目之间的布局中插入水平空白空间
    layout.use_property_split = True
    layout.use_property_decorate = False

    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    row = layout.row()
    # col = row.column()
    # col.label(text="DDS格式情况")

    col = row.column()
    col.label(text="DDS->PNG，格式设置")
    col.prop(addon_prefs.png, "Layer")
    col.prop(addon_prefs.png, "Mipmap")
    col.prop(addon_prefs.png, "Data_Type")
    match addon_prefs.png.Data_Type:
        case "UNORM": col.prop(addon_prefs.png, "UNORM_Format")
        case "SRGB": col.prop(addon_prefs.png, "SRGB_Format")

    row = layout.row()
    operator = addon_prefs
    col = row.column()
    operator_add = col.operator("ZHUFILE_OT_func_add_texture_batch_convert", text="添加所选文件")
    col.template_list("ZHUFILE_UL_选择文件列表", "", operator, "选择文件组", operator, "选择集索引") # operator = self [operator, "选择集索引"] == operator.选择集索引
    
    col = row.column()
    operator_run = col.operator("ZHUFILE_OT_func_run_texture_batch_convert", text="转换所选文件")
    col.template_list("ZHUFILE_UL_保存文件列表", "", operator, "保存文件组", operator, "保存集索引") # 后面测试下operator改bpy.types.PropertyGroup是否可行，以及如何让operator一直存在不被销毁，以及再draw之外能否新建实例
    layout.operator("ZHUFILE_OT_func_clear_texture_batch_convert", text="清空")


