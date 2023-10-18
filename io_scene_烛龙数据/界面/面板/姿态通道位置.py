import bpy



class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    位置导入空间: bpy.props.EnumProperty(
        items = (
            ('Auto_Space',  "Auto_Space", ""),          
            ('Bone_Space',  "Bone_Space", ""),
            ('Basis_Space', "Basis_Space", ""),
            ),
        default = 'Auto_Space',
        )



    坐标系变换模式: bpy.props.EnumProperty(
        items = (
            ('自动处理', "自动处理", ""),
            ('原始数据', "原始数据", ""),
            ('手动设置', "手动设置", ""),
            ),
        default = '自动处理',
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
        default = 'Z',
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
        default = 'Y',
        )



class ZHUFILE_OT_姿态通道位置_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_action_location"
    bl_label  = "选项设置"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.姿态通道位置)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ZHUFILE_PT_姿态通道位置_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_action_location_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "姿态通道位置.选项设置"
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 13

    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.姿态通道位置)


def draw(self, 姿态通道位置):
    layout = self.layout

    layout.use_property_split = True
    layout.use_property_decorate = False

    layout.label(text="Blender Basis 空间，位置变换")
    box = layout.box()
    box.prop(姿态通道位置, "位置导入空间")
    if 姿态通道位置.位置导入空间 != "Auto_Space":
        draw_空间提示(box)
    
    box = layout.box()
    box.prop(姿态通道位置, "坐标系变换模式")
    if 姿态通道位置.坐标系变换模式 == "手动设置":
        draw_坐标变换(box, 姿态通道位置)
        draw_坐标提示(box)


def draw_坐标变换(box, 姿态通道位置):
    row = box.row()
    col = row.column()
    col.label(text="向前")
    col.label(text=" +X")

    col = row.column()
    col.label(text="向右")
    col.label(text=" +Y")

    col = row.column()
    col.label(text="向上")
    col.label(text=" +Z")

    col = row.column()
    col.label(text="向前")
    col.prop(姿态通道位置, "坐标系向前", text="")

    col = row.column()
    col.label(text="向右")
    col.prop(姿态通道位置, "坐标系向右", text="")

    col = row.column()
    col.label(text="向上")
    col.prop(姿态通道位置, "坐标系向上", text="")


def draw_空间提示(box):
    box.label(text=" Maybe it\'s wrong, but it works!") 
    # row = box.row()
    # row.label(text=" fbx_loc_space: [bone]"), row.label(text=" fbx_rot_space: [bone]") 
    # row = box.row()
    # row.label(text=" kf_loc_space: [bone]"), row.label(text=" kf_rot_space: [bone]")
    # row = box.row()
    # row.label(text=" xsm_loc_space: [bone]"), row.label(text=" xsm_rot_space: [bone]")
    row = box.row()
    row.label(text=" hka_loc_space: [basis]"), row.label(text=" hka_rot_space: [bone]")
    row = box.row()
    row.label(text=" hkx_loc_space: [bone]"), row.label(text=" hkx_rot_space: [bone]")


def draw_坐标提示(box):
    box.label(text=" Blender中: 3DView[XZ-Y] == Basis[XYZ],  3DView[XYZ] == Basis[X-ZY]") 
    box.label(text=" fbx_action_loc: [XYZ] -> [YZ-X] or [ZY-X] ") 
    row = box.row()
    row.label(text=" hka_loc: [XYZ] -> [-YXZ]"), row.label(text=" hkx_loc: [XYZ] -> [-YXZ]")
    