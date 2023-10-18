import bpy


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    弹窗显示模式: bpy.props.EnumProperty(
        items = (
            ('点击弹窗', "点击弹窗", ""),
            ('悬浮弹窗', "悬浮弹窗", ""),
            ('嵌入窗口', "嵌入窗口", ""),
            ),
        default = '点击弹窗',
        )


class ZHUFILE_PT_UI类型(bpy.types.Panel):
    # bl_idname = 
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "UI类型"
    # bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"


    def draw(self, context):
        operator = context.space_data.active_operator
        UI类型 = operator.UI类型
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(UI类型, "弹窗显示模式")



