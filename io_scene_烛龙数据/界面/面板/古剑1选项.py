import bpy


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    导入头发裙子动画: bpy.props.BoolProperty(
        name = "导入头发裙子动画",
        default = True,
    )

    导入动画合并: bpy.props.BoolProperty(
        name = "导入动画合并",
        default = False,
    )

class ZHUFILE_PT_古剑1选项(bpy.types.Panel):
    # bl_idname = 
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "古剑1选项"
    bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_remain_setting"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"


    def draw(self, context):
        operator = context.space_data.active_operator
        古剑1选项 = operator.古剑1选项
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(古剑1选项, "导入动画合并")
        layout.prop(古剑1选项, "导入头发裙子动画")

