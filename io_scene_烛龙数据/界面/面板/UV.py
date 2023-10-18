import bpy

class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    处理模式: bpy.props.EnumProperty(
        items=(
            ('自动处理', "自动处理", ""),
            ('原始数据', "原始数据", ""),
            ('手动设置', "手动设置", ""),
            ),
        default='自动处理',
        )

    U轴翻转: bpy.props.BoolProperty(
        name = "U轴翻转",
        description = "将U(X)轴数据*(-1), V(Y)轴数据不变",
        default = False,
        )

    V轴翻转: bpy.props.BoolProperty(
        name = "V轴翻转",
        description = "将V(Y)轴数据*(-1), U(X)轴数据不变",
        default = False,
        )


    U轴移动: bpy.props.EnumProperty(
        items = (
            ( "2.0",  "2.0", ""),
            ( "1.5",  "1.5", ""),
            ( "1.0",  "1.0", ""),
            ( "0.5",  "0.5", ""),
            ( "0.0",  "0.0", ""),
            ("-0.5", "-0.5", ""),
            ("-1.0", "-1.0", ""),
            ("-1.5", "-1.5", ""),
            ("-2.0", "-2.0", ""),
            ),
        default = '0.0',
        )

    V轴移动: bpy.props.EnumProperty(
        items = (
            ( "2.0",  "2.0", ""),
            ( "1.5",  "1.5", ""),
            ( "1.0",  "1.0", ""),
            ( "0.5",  "0.5", ""),
            ( "0.0",  "0.0", ""),
            ("-0.5", "-0.5", ""),
            ("-1.0", "-1.0", ""),
            ("-1.5", "-1.5", ""),
            ("-2.0", "-2.0", ""),
            ),
        default = '0.0',
        )

    U轴负域镜像正域: bpy.props.BoolProperty(
        name = "U轴负域镜像正域",
        description = "将U(X)轴<0的部分镜像到正域(<0部分*(-1)), V(Y)轴数据不变",
        default = False,
        )

    V轴负域镜像正域: bpy.props.BoolProperty(
        name = "V轴负域镜像正域",
        description = "将V(Y)轴<0的部分镜像到正域(<0部分*(-1)), U(X)轴数据不变",
        default = False,
        )


class ZHUFILE_OT_UV_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_uv"
    bl_label  = "选项设置"                # 弹出的文件浏览器的确定按钮上显示的文本

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.UV)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)



class ZHUFILE_PT_UV_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_uv_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "uv.选项设置"
    bl_options = {'INSTANCED'} # bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x = 13



    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.UV)


def draw(self, UV):
    layout = self.layout
    # layout.active = UV.启用

    layout.use_property_split = True
    layout.use_property_decorate = False

    # layout.prop(UV, "启用", text="启用设置")

    layout.prop(UV, "处理模式")
    if UV.处理模式 == "手动设置":
        row = layout.row()
        row.use_property_split = False
        col = row.box()
        col.label(text="U轴")
        col.prop(UV, "U轴翻转",         text="翻转")
        col.prop(UV, "U轴负域镜像正域", text="负域镜像正域")
        col.prop(UV, "U轴移动",         text="移动")

        col = row.box()
        col.label(text="V轴")
        col.prop(UV, "V轴翻转",         text="翻转")
        col.prop(UV, "V轴负域镜像正域", text="负域镜像正域")
        col.prop(UV, "V轴移动",         text="移动")



