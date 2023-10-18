import bpy
from ... import 数据


class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    坐标系旋转模式: bpy.props.EnumProperty(
        items = (
            ('自动处理', "自动处理", ""),
            ('原始数据', "原始数据", ""),
            ('手动设置', "手动设置", ""),
            ),
        default = '自动处理',
        )


    绕X轴旋转: bpy.props.EnumProperty(
        items = (
            ( "270°",   "270°", ""),
            ( "180°",   "180°", ""),
            (  "90°",    "90°", ""),
            (   "0°",     "0°", ""),
            ( "-90°",   "-90°", ""),
            ("-180°",  "-180°", ""),
            ("-270°",  "-270°", ""),
            ),
        default = '0°',
        )


    绕Y轴旋转: bpy.props.EnumProperty(
        items = (
            ( "270°",   "270°", ""),
            ( "180°",   "180°", ""),
            (  "90°",    "90°", ""),
            (   "0°",     "0°", ""),
            ( "-90°",   "-90°", ""),
            ("-180°",  "-180°", ""),
            ("-270°",  "-270°", ""),
            ),
        default = '0°',
        )


    绕Z轴旋转: bpy.props.EnumProperty(
        items = (
            ( "270°",   "270°", ""),
            ( "180°",   "180°", ""),
            (  "90°",    "90°", ""),
            (   "0°",     "0°", ""),
            ( "-90°",   "-90°", ""),
            ("-180°",  "-180°", ""),
            ("-270°",  "-270°", ""),
            ),
        default = '0°',
        )


class ZHUFILE_OT_旋转_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_rotation"
    bl_label  = "选项设置"                # 弹出的文件浏览器的确定按钮上显示的文本

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.旋转)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


   
class ZHUFILE_PT_旋转_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_rotation_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "旋转.选项设置"
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 13
    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.旋转)



def draw(self, 旋转):
    layout = self.layout

    layout.use_property_split = True
    layout.use_property_decorate = False


    layout.label(text="文件 Local 空间。逆时针旋转为正值，顺时针为负值")
    layout.prop(旋转, "坐标系旋转模式")
    if 旋转.坐标系旋转模式 == "手动设置":
        row = layout.row()
        col = row.column()
        col.label(text=" 绕X轴旋转")
        col.prop(旋转, "绕X轴旋转", text="")

        col = row.column()
        col.label(text=" 绕Y轴旋转")
        col.prop(旋转, "绕Y轴旋转", text="")

        col = row.column()
        col.label(text=" 绕Z轴旋转")
        col.prop(旋转, "绕Z轴旋转", text="")


