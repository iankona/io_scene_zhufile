import bpy


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    # 游戏标签: bpy.props.EnumProperty(
    #     items=(
    #         ('自动推测',                   "自动推测",                   ""),
    #         ('古剑奇谭：琴心剑魄今何在',   "古剑奇谭：琴心剑魄今何在",   ""),
    #         ('古剑奇谭二：永夜初晗凝碧天', "古剑奇谭二：永夜初晗凝碧天", ""),
    #         ('古剑奇谭三：梦付千秋星垂野', "古剑奇谭三：梦付千秋星垂野", ""),
    #         ('X4: Foundations',            "X4: Foundations",            ""),
    #         ('The Witcher 3: Wild Hunt',   "The Witcher 3: Wild Hunt",   ""),
    #         ),
    #     default = '自动推测',
    #     )


    导入模式: bpy.props.EnumProperty(
        items = (
            ('新建单独选择集', "新建单独选择集", ""),
            ('引用现有选择集', "引用现有选择集", ""),
            ),
        default = '新建单独选择集',
        )

    名称替换: bpy.props.EnumProperty(
        items = (
            ('原始名称'       , "原始名称"       , ""),
            ('替换古剑1名称'  , "替换古剑1名称"  , ""),
            ('替换古剑2名称'  , "替换古剑2名称"  , ""),
            ('替换古剑3名称'  , "替换古剑3名称"  , ""),
            ('替换古剑1古剑2名称', "替换古剑1古剑2名称", ""),
            ('替换古剑1古剑3名称', "替换古剑1古剑3名称", ""),
            ('替换古剑2古剑3名称', "替换古剑2古剑3名称", ""),
            ('替换古剑1古剑2古剑3名称', "替换古剑1古剑2古剑3名称", ""),
            ),
        default = '替换古剑1古剑2古剑3名称',
        )


    所选范围扩展: bpy.props.EnumProperty(
        items = (
            ('自动推测', "自动推测", "自动推测并补齐未选文件，并划分好选择集..."),
            ('当前多选', "当前多选", "仅导入当前所选文件"),
            ),
        default = '当前多选',
        )



class ZHUFILE_OT_选择_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_collection"
    bl_label  = "选项设置"   

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.选择)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ZHUFILE_PT_选择_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_collection_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "选择集.选项设置" # 不能删除
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 13

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.选择)

def draw(self, 选择):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    # layout.prop(选择, "游戏标签")
    layout.prop(选择, "导入模式")
    layout.prop(选择, "名称替换")
    layout.prop(选择, "所选范围扩展")





