import bpy

class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    材质导入模式: bpy.props.EnumProperty(
        items = (
            ('新建单独材质', "新建单独材质", ""),
            ('引用现有材质', "引用现有材质", ""),
            ),
        default = '新建单独材质',
        )

    贴图导入模式: bpy.props.EnumProperty(
        items = (
            ('新建单独贴图', "新建单独贴图", ""),
            ('引用现有贴图', "引用现有贴图", ""),
            ),
        default = '引用现有贴图',
        )


    法线导入模式: bpy.props.EnumProperty(
        items = (
            ('自动处理', "自动处理", ""),
            ('手动设置', "手动设置", ""),
            ),
        default = '自动处理',
        )

    法线贴图空间: bpy.props.EnumProperty(
        items = (
            ("切线空间", "切线空间", "TANGENT"),
            ("物体空间", "物体空间", ""),
            ("世界空间", "世界空间", ""),
            ("Blender物体空间", "Blender物体空间", ""),
            ("Blender世界空间", "Blender世界空间", ""),
        ),
        default = "世界空间",
        )





    材质节点布局: bpy.props.EnumProperty(
        items = (
            ('列表布局', "列表布局", ""),
            ('行高布局', "行高布局", ""),
            ('网格布局', "网格布局", ""),
            ),
        default = '列表布局',
        )
    
    x: bpy.props.IntProperty(
        name = '', 
        description = '', 
        default = 0,
        )
    
    y: bpy.props.IntProperty(
        name = '', 
        description = '', 
        default = 0,
        )
    
    padx: bpy.props.IntProperty(
        name = '', 
        description = '', 
        default = 50,
        min = 0,
        max = 1000,
        )

    pady: bpy.props.IntProperty(
        name = '', 
        description = '', 
        default = 50,
        min = 0,
        max = 1000,
        )
    
    rowsize: bpy.props.IntProperty(
        name = '', 
        description = '', 
        default = 300,
        min = 0,
        max = 1000,
        )
    
    columnsize: bpy.props.IntProperty(
        name = '', 
        description = '', 
        default = 300,
        min = 0,
        max = 1000,
        )


    

class ZHUFILE_OT_材质_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_material"
    bl_label  = "选项设置"                # 弹出的文件浏览器的确定按钮上显示的文本

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.材质)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    

class ZHUFILE_PT_材质_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_material_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "材质.选项设置"
    bl_options = {'INSTANCED'} # bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x = 13

    
    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        operator = context.space_data.active_operator
        draw(self, operator.材质)


def draw(self, 材质):
    layout = self.layout

    layout.use_property_split = True
    layout.use_property_decorate = False

    box = layout.box()
    box.prop(材质, "材质导入模式")
    
    box = layout.box()
    box.prop(材质, "贴图导入模式")

    box = layout.box()
    box.prop(材质, "法线导入模式")
    if 材质.法线导入模式 == "手动设置": box.prop(材质, "法线贴图空间")

    box = layout.box()
    box.prop(材质, "材质节点布局")

    match 材质.材质节点布局:
        case '列表布局': draw_list(box, 材质)
        case '行高布局': draw_list(box, 材质)
        case '网格布局': draw_mesh(box, 材质)


def draw_list(box, 材质):
    row = box.row()

    col = row.column()
    col.label(text=" start_x") # 布局起点
    col.prop(材质, "x", text="")

    col = row.column()
    col.label(text=" start_y") # 布局起点
    col.prop(材质, "y", text="")

    col = row.column()
    col.label(text=" pad_x")
    col.prop(材质, "padx", text="")

    col = row.column()
    col.label(text=" pad_y")
    col.prop(材质, "pady", text="")
    

def draw_mesh(box, 材质):
    row = box.row()

    col = row.column()
    col.label(text=" start_x") # 布局起点
    col.prop(材质, "x", text="")

    col = row.column()
    col.label(text=" start_y") # 布局起点
    col.prop(材质, "y", text="")

    col = row.column()
    col.label(text=" rowheight")
    col.prop(材质, "rowsize", text="")

    col = row.column()
    col.label(text=" columnwidth")
    col.prop(材质, "columnsize", text="")

