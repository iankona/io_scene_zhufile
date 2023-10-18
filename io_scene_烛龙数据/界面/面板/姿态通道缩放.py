import bpy



class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    缩放导入空间: bpy.props.EnumProperty(
        items = (
            ('Auto_Space',  "Auto_Space", ""),          
            ('Bone_Space',  "Bone_Space", ""),
            ('Basis_Space', "Basis_Space", ""),
            ),
        default = 'Auto_Space',
        )



    坐标系缩放模式: bpy.props.EnumProperty(
        items = (
            ('自动处理', "自动处理", ""),
            ('原始数据', "原始数据", ""),
            ('手动设置', "手动设置", ""),
            ),
        default = '自动处理',
        )

    scale_x: bpy.props.FloatProperty(
        name = 'scale_x', 
        description = '', 
        default = 1.0,
        min = 0.001,
        max = 1000.0,
        )
    
    scale_y: bpy.props.FloatProperty(
        name = 'scale_y', 
        description = '', 
        default = 1.0,
        min = 0.001,
        max = 1000.0,
        )
    
    scale_z: bpy.props.FloatProperty(
        name = 'scale_z', 
        description = '', 
        default = 1.0,
        min = 0.001,
        max = 1000.0,
        )
    

class ZHUFILE_OT_姿态通道缩放_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_action_scale"
    bl_label  = "选项设置"                # 弹出的文件浏览器的确定按钮上显示的文本

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.姿态通道缩放)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)



class ZHUFILE_PT_姿态通道缩放_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_action_scale_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "姿态通道缩放.选项设置"
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 13

    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.姿态通道缩放)


def draw(self, 姿态通道缩放):
    layout = self.layout

    layout.use_property_split = True
    layout.use_property_decorate = False

    layout.label(text="Blender Basis 空间，位置缩放")
    layout.prop(姿态通道缩放, "缩放导入空间")
    layout.prop(姿态通道缩放, "坐标系缩放模式")
    if 姿态通道缩放.坐标系缩放模式 == "手动设置":
        row = layout.row()
        col = row.column()
        col.label(text=" X")
        col.prop(姿态通道缩放, "scale_x", text="")

        col = row.column()
        col.label(text="Y")
        col.prop(姿态通道缩放, "scale_y", text="")

        col = row.column()
        col.label(text="Z")
        col.prop(姿态通道缩放, "scale_z", text="")
