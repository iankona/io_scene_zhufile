import bpy
from .. import 数据
from .  import 面板

class ZHUFILE_PT_选择集(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_collection"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "选择集"
    # bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_collection") 
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_collection_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.选择.draw(self, operator.选择)



class ZHUFILE_PT_材质(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_material"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "材质"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_collection"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_material")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_material_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.材质.draw(self, operator.材质)


class ZHUFILE_PT_UV(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_uv"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "UV"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_material"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text=" ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_uv")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_uv_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.UV.draw(self, operator.UV)


class ZHUFILE_PT_贴图(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_texture"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "贴图"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_material"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text=" ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_texture")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_texture_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.贴图.draw(self, operator.贴图)



class ZHUFILE_PT_变换(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_transformation"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "比例、坐标系变换"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_collection"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_transformation") 
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_transformation_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.变换.draw(self, operator.变换)


class ZHUFILE_PT_旋转(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_rotation"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "旋转"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_transformation"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text=" ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_rotation") 
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_rotation_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.旋转.draw(self, operator.旋转)


class ZHUFILE_PT_骨架(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_armature"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "骨架"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_rotation"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text="　  ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_armature")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_armature_property", text="选项设置")

    def draw(self, context):
        面板.骨架.sets(self, context)
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.骨架.draw(self, operator.骨架)


class ZHUFILE_PT_网格(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_mesh"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "网格"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_rotation"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text="　  ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_mesh")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_mesh_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.网格.draw(self, operator.网格)


class ZHUFILE_PT_姿态(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_action"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "动作"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_transformation"
    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text=" ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_action")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_action_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.姿态.draw(self, operator.姿态)


class ZHUFILE_PT_姿态通道位置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_action_location"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "姿态通道位置"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_action"
    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text="　  ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_action_location")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_action_location_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.姿态通道位置.draw(self, operator.姿态通道位置)


class ZHUFILE_PT_姿态通道旋转(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_action_rotation"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "姿态通道旋转"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_action"
    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text="　  ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_action_rotation")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_action_rotation_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.姿态通道旋转.draw(self, operator.姿态通道旋转)


class ZHUFILE_PT_姿态通道缩放(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_action_scale"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "姿态通道缩放"
    # bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_action"
    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw_header(self, context):
        self.layout.label(text="　  ")
        match 数据.变量.UI类型.弹窗显示模式:
            case "点击弹窗": self.layout.operator("zhufile.property_action_scale")
            case "悬浮弹窗": self.layout.popover(panel="FILEBROWSER_PT_zhufile_action_scale_property", text="选项设置")

    def draw(self, context):
        operator = context.space_data.active_operator
        if 数据.变量.UI类型.弹窗显示模式 == "嵌入窗口": 面板.姿态通道缩放.draw(self, operator.姿态通道缩放)



class ZHUFILE_PT_其他设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_remain_setting"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "其他选项"
    # bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        pass

