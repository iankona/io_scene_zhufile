import bpy


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    骨架选择模式: bpy.props.EnumProperty(
        items = (
            ("当前选中(多选)", "当前选中(多选)", "多选骨架对象"),
            ("armatures[:]",   "armatures[:]",   "所有骨架对象"),
            ("armatures[0]",   "armatures[0]",   "最早建立的骨架"),
            ("armatures[-1]",  "armatures[-1]",  "最后建立的骨架"),
            ),
        default = '当前选中(多选)',
        )
    

    开启测试特性: bpy.props.BoolProperty(
        name = "开启测试特性",
        default = False,
        description = '', 
    )


    动画合并模式: bpy.props.EnumProperty(
        items = (
            ('原始数据', "原始数据", "未合并，各自分开的文件动画导入"),
            ('姿态相加', "姿态相加", "相同骨骼的同一帧数据相加"),
            ('姿态顾前', "姿态顾前", "相同骨骼的同一帧数据，多选时，只保留最初选的文件姿态"),
            ('姿态顾后', "姿态顾后", "相同骨骼的同一帧数据，多选时，只保留最后选的文件姿态"),
            ),
        default = '原始数据',
        )


    动作导入通道: bpy.props.EnumProperty(
        items = (
            ("Null",      "Null",      ""),
            ("Loc",       "Loc",       ""),
            ("Rot",       "Rot",       ""),
            ("Sca",       "Sca",       ""),
            ("LocRot",    "LocRot",    ""),
            ("LocSca",    "LocSca",    ""),
            ("RotSca",    "RotSca",    ""),
            ("LocRotSca", "LocRotSca", "位置+四元数旋转+缩放"),
            ),
        default = 'LocRotSca',
        )


    动画导入模式: bpy.props.EnumProperty(
        items = (
            ('引用现有Action', "引用现有Action", ""),
            ('新建单独Action', "新建单独Action", ""),
            ),
        default = '新建单独Action',
        )
    

# operator = None

class ZHUFILE_OT_姿态_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_action"
    bl_label  = "选项设置" 

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        global operator 
        operator = context.space_data.active_operator
        draw(self, operator.姿态)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)



class ZHUFILE_PT_姿态_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_action_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "动作.选项设置"
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 13

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"


    def draw(self, context):
        # global operator 
        operator = context.space_data.active_operator
        draw(self, operator.姿态)



def draw(self, 姿态):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    box = layout.box()
    box.prop(姿态, "骨架选择模式")

    if 姿态.开启测试特性:
        box = layout.box()
        row = box.row()
        row.use_property_split = False
        row.prop(姿态, "开启测试特性")
        # row.label(text="多个动画文件合并成1个动画导入", icon='OBJECT_DATAMODE')
        box.prop(姿态, "动画合并模式")
    else:
        layout.prop(姿态, "开启测试特性")

    box = layout.box()
    box.prop(姿态, "动画导入模式")
    box.prop(姿态, "动作导入通道")



