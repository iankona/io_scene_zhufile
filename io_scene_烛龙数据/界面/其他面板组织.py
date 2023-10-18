import bpy
from .. import 数据
from .  import 其他面板



class ZHUFILE_PT_其他功能(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_other_function"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "其他功能"
    # bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        pass

class ZHUFILE_PT_贴图_批量转换(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_texture_batch_convert"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "贴图批量转换"
    bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_other_function"

    # 面板不能挂载属性
    # 选择集索引: bpy.props.IntProperty(name="选择集索引", default=0)
    # 选择集文件: bpy.props.CollectionProperty(type=bpy.types.选择文件)
    # 保存集索引: bpy.props.IntProperty(name="保存集索引", default=0)
    # 保存集文件: bpy.props.CollectionProperty(type=bpy.types.保存文件)
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        # self.layout.label(text="　  ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_texture_batch_convert")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_texture_batch_convert_property", text="选项设置") # 注意：panel ID 不能太长，会出现找不到面板错误

    def draw(self, context):
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 其他面板.贴图批量转换.draw(self)


class ZHUFILE_PT_骨架_切换动作(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_armature_switch_action"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "骨架切换动作"
    bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_other_function"

    # 面板不能挂载属性
    # 选择集索引: bpy.props.IntProperty(name="选择集索引", default=0)
    # 选择集文件: bpy.props.CollectionProperty(type=bpy.types.选择文件)
    # 保存集索引: bpy.props.IntProperty(name="保存集索引", default=0)
    # 保存集文件: bpy.props.CollectionProperty(type=bpy.types.保存文件)
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        # self.layout.label(text="　  ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_armature_switch_action")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_armature_switch_action_property", text="选项设置") # 注意：panel ID 不能太长，会出现找不到面板错误

    def draw(self, context):
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 其他面板.骨架切换动作.draw(self)