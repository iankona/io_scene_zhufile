import bpy


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    pass
    # 导入缺UV网格: bpy.props.BoolProperty(
    #     name = "导入缺UV网格",
    #     default = True,
    # )

class ZHUFILE_PT_古剑2选项(bpy.types.Panel):
    # bl_idname = 
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "古剑2选项"
    bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_remain_setting"
    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"


    def draw(self, context):
        layout = self.layout
        operator = context.space_data.active_operator
        古剑2选项 = operator.古剑2选项


        layout.use_property_split = True
        layout.use_property_decorate = False

        # layout.prop(古剑2选项, "导入缺UV网格")
        layout.label(text="标签")