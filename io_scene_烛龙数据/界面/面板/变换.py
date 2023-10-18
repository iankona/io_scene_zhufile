import bpy


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    坐标系变换模式: bpy.props.EnumProperty(
        items=(
            ('自动处理', "自动处理", ""),
            ('原始数据', "原始数据", ""),
            ('手动设置', "手动设置", ""),
            ),
        default='自动处理',
        )


    坐标系向前: bpy.props.EnumProperty(
        items = (
            ( "X",  "X", ""),
            ("-X", "-X", ""),
            ( "Y",  "Y", ""),
            ("-Y", "-Y", ""),
            ( "Z",  "Z", ""),
            ("-Z", "-Z", ""),
            ),
        default='-Y',
        )


    坐标系向右: bpy.props.EnumProperty(
        items = (
            ( "X",  "X", ""),
            ("-X", "-X", ""),
            ( "Y",  "Y", ""),
            ("-Y", "-Y", ""),
            ( "Z",  "Z", ""),
            ("-Z", "-Z", ""),
            ),
        default='X',
        )


    坐标系向上: bpy.props.EnumProperty(
        items = (
            ( "X",  "X", ""),
            ("-X", "-X", ""),
            ( "Y",  "Y", ""),
            ("-Y", "-Y", ""),
            ( "Z",  "Z", ""),
            ("-Z", "-Z", ""),
            ),
        default='Z',
        )

    坐标系缩放模式: bpy.props.EnumProperty(
        items = (
            ('自动处理', "自动处理", ""),
            ('原始数据', "原始数据", ""),
            ('手动设置', "手动设置", ""),
            ),
        default = '自动处理',
        )

    缩放系数: bpy.props.EnumProperty(
        items = (
            ('0.001' , "0.001" , ""),
            ('0.01'  , "0.01"  , ""),
            ('0.1'   , "0.1"   , ""),
            ('1.0'   , "1.0"   , ""),
            ('10.0'  , "10.0"  , ""),
            ('100.0' , "100.0" , ""),
            ('1000.0', "1000.0", ""),
            ),
        default = '0.01',
        )



class ZHUFILE_OT_变换_选项设置(bpy.types.Operator):
    """test"""
    bl_idname = "zhufile.property_transformation"
    bl_label  = "选项设置"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.变换)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ZHUFILE_PT_变换_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_transformation_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "变换集.选项设置"
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 16 # 因该项设置是发生在注册类时，不能访问到 operator.UI类型，故不能 = 数据.变量.UI类型.悬浮窗口长度
    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.变换)


def draw(self, 变换):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    box = layout.box()
    box.label(text="文件 Local 空间，坐标变换、骨骼轴向变换")
    box.prop(变换, "坐标系变换模式") # 主要是为了嵌入窗口文字能靠左边，故是坐标系，不是坐标
    if 变换.坐标系变换模式 == "手动设置": draw_坐标变换(box, 变换)

    box = layout.box()
    box.label(text="文件 Local 空间，位置坐标缩放")
    box.prop(变换, "坐标系缩放模式")
    if 变换.坐标系缩放模式 == "手动设置": box.prop(变换, "缩放系数")
    
    if 变换.坐标系变换模式 == "手动设置": draw_坐标提示(layout.box())


def draw_坐标变换(box, 变换):
    row = box.row()
    col = row.column()
    col.label(text=" 向前")
    col.label(text=" +X")

    col = row.column()
    col.label(text="向右")
    col.label(text=" +Y")

    col = row.column()
    col.label(text="向上")
    col.label(text=" +Z")

    col = row.column()
    col.label(text="向前")
    col.prop(变换, "坐标系向前", text="")

    col = row.column()
    col.label(text="向右")
    col.prop(变换, "坐标系向右", text="")

    col = row.column()
    col.label(text="向上")
    col.prop(变换, "坐标系向上", text="")


def draw_坐标提示(box):
    box.label(text=" FBX_models: [XYZ] -> [-YXZ] -> [0°, 90°, 0°] -> [1.00]")
    box.label(text=" FBX_action: [XYZ] -> [-YXZ] -> [1.00]")
    box.label(text=" NIF: [XYZ] -> [-YXZ] -> [0.01]")
    box.label(text=" KF: [XYZ] -> [-YXZ] -> [0.01]")
    box.label(text=" XAC: [XYZ] -> [-YXZ] -> [180°, 90°, 0°] -> [0.01]")
    box.label(text=" XSM: [XYZ] -> [-YXZ] -> [0.01]")    
    box.label(text=" VMESH: [XYZ] -> [-YXZ] -> [0.01]")
    box.label(text=" MODEL: [XYZ] -> [-YXZ] -> [0.01]")
    box.label(text=" HKA: [XYZ] -> [-YXZ] -> [0.01]")
    box.label(text=" HKX: [XYZ] -> [-YXZ] -> [1.00]")
    box.label(text=" SRT: [XYZ] -> [XYZ] -> [0.01]")



