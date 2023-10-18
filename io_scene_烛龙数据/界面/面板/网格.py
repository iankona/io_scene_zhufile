import bpy



class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    导入缺UV网格: bpy.props.BoolProperty(
        name = "导入缺UV网格",
        default = True,
    )

    分面模式: bpy.props.EnumProperty(
        items = (
            ('原始数据', "原始数据", ""),
            ('自动分面', "自动分面", ""),
            ),
        default = '原始数据',
        )


class ZHUFILE_OT_网格_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_mesh"
    bl_label  = "选项设置"                # 弹出的文件浏览器的确定按钮上显示的文本

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.网格)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ZHUFILE_PT_网格_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_mesh_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "网格.选项设置"
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 13


    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"


    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.网格)



def draw(self, 网格):
    layout = self.layout

    layout.use_property_split = True
    layout.use_property_decorate = False
    layout.prop(网格, "导入缺UV网格")
    # layout.prop(网格, "分面模式")



