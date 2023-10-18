import bpy



class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    贴图格式: bpy.props.EnumProperty(
        items = (
            ('dds', "dds", ""),
            ('png', "png", ""),
            ),
        default = 'dds',
        )


    转换程序: bpy.props.EnumProperty(
        items = (
            ("ImageViewer", "ImageViewer", ""),
            ),
        default = 'ImageViewer',
        )

    转换形式: bpy.props.EnumProperty(
        items = (
            ("重新生成贴图", "重新生成贴图", ""),
            ("引用现有贴图", "引用现有贴图", ""),
            ),
        default = '引用现有贴图',
        )


    Layer: bpy.props.EnumProperty(
        items = (
            ("Layer_0", "Layer_0", ""),
            ),
        default='Layer_0',
        )

    Mipmap: bpy.props.EnumProperty(
        items = (
            ("Mipmap_0",  "Mipmap_0",  ""),
            ("Mipmap_1",  "Mipmap_1",  ""),
            ("Mipmap_2",  "Mipmap_2",  ""),
            ("Mipmap_3",  "Mipmap_3",  ""),
            ("Mipmap_4",  "Mipmap_4",  ""),
            ("Mipmap_5",  "Mipmap_5",  ""),
            ("Mipmap_6",  "Mipmap_6",  ""),
            ("Mipmap_7",  "Mipmap_7",  ""),
            ("Mipmap_8",  "Mipmap_8",  ""),
            ("Mipmap_9",  "Mipmap_9",  ""),
            ("Mipmap_10", "Mipmap_10", ""),
            ("Mipmap_11", "Mipmap_11", ""),
            ("Mipmap_12", "Mipmap_12", ""),
            ),
        default = 'Mipmap_0',
        )

    Data_Type: bpy.props.EnumProperty(
        items = (
            ("UNORM", "UNORM", ""),
            ("SRGB",  "SRGB",  ""),
            ),
        default = 'UNORM',
        )

    UNORM_Format: bpy.props.EnumProperty(
        items = (
            ("R8_UNORM",     "R8_UNORM",     ""),
            ("RA8_UNORM",    "RA8_UNORM",    ""),
            ("RGB8_UNORM",   "RGB8_UNORM",   ""),
            ("RGBA8_UNORM",  "RGBA8_UNORM",  ""),
            ("R16_UNORM",    "R16_UNORM",    ""),
            ("RA16_UNORM",   "RA16_UNORM",   ""),
            ("RGB16_UNORM",  "RGB16_UNORM",  ""),
            ("RGBA16_UNORM", "RGBA16_UNORM", ""),
            ),
        default = 'RGBA8_UNORM',
        )

    SRGB_Format: bpy.props.EnumProperty(
        items = (
            ("R8_SRGB",    "R8_SRGB",    ""),
            ("RA8_SRGB",   "RA8_SRGB",   ""),
            ("RGB8_SRGB",  "RGB8_SRGB",  ""),
            ("RGBA8_SRGB", "RGBA8_SRGB", ""),
            ),
        default = 'RGBA8_SRGB',
        )



class ZHUFILE_OT_贴图_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_texture"
    bl_label  = "选项设置" 

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.贴图)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)



class ZHUFILE_PT_贴图_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_texture_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "贴图.选项设置"
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 13


    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.贴图)


def draw(self, 贴图):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    layout.prop(贴图, "贴图格式")
    match 贴图.贴图格式:
        case "dds": pass
        case "png": draw_png(self, 贴图)


def draw_png(self, 贴图):
    layout = self.layout

    layout.use_property_split = True
    layout.use_property_decorate = False

    layout.prop(贴图, "转换程序")
    layout.prop(贴图, "转换形式")
    layout.prop(贴图, "Layer")
    layout.prop(贴图, "Mipmap")

    box = layout.box()
    box.prop(贴图, "Data_Type")

    match 贴图.Data_Type:
        case "UNORM": box.prop(贴图, "UNORM_Format")
        case "SRGB": box.prop(贴图, "SRGB_Format")


