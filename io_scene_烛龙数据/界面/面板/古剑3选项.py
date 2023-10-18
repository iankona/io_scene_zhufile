import bpy


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    # 材质导入节点组: bpy.props.EnumProperty(
    #     items = (
    #         ('星月夜曲组', "星月夜曲组", "感谢贴吧用户：星月夜曲组，提供的材质节点组合"),
    #         ('占位符号组', "占位符号组", ""),
    #         ),
    #     default = '占位符号组',
    #     )


    眼睛开启高光: bpy.props.BoolProperty(
        name = "眼睛开启高光",
        default = False,
    )


    表情导入模式: bpy.props.EnumProperty(
        items = (
            ("形态键左值", "形态键左值", ""),
            ("形态键均值", "形态键均值", ""),
            ("形态键右值", "形态键右值", ""),
        ),
        default = "形态键均值",
        )



class ZHUFILE_PT_古剑3选项(bpy.types.Panel):
    # bl_idname = 
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "古剑3选项"
    bl_options = {'DEFAULT_CLOSED'}

    bl_parent_id = "FILEBROWSER_PT_zhufile_remain_setting"

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"


    def draw(self, context):
        operator = context.space_data.active_operator
        古剑3选项 = operator.古剑3选项
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(古剑3选项, "眼睛开启高光")
        layout.prop(古剑3选项, "表情导入模式")

