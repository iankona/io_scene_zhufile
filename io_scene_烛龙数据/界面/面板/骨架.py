import bpy

class ZHUFILE_PROP_UI组(bpy.types.PropertyGroup):
    骨骼长度处理模式: bpy.props.EnumProperty(
        items = (
            ('自动处理', "自动处理", ""),
            ('原始数据', "原始数据", ""),
            ('手动设置', "手动设置", ""),
            ),
        default = '自动处理',
        )


    骨骼长度: bpy.props.FloatProperty(
        name = '骨骼长度', 
        description = '', 
        default = 2.0,
        min = 0.0,
        max = 1000.0,
        )

    骨架导入模式: bpy.props.EnumProperty(
        items = (
            ('合并骨架', "合并骨架", "将所选(多选)的文件里的骨架，全部合并到同一个骨架里，为原来的古剑3的“同一个骨架”功能扩展而来"),
            ('各自骨架', "各自骨架", "原始数据，模型各自对应文件里的骨架，不合并"),
            ('略过骨架', "略过骨架", "不导入所选(多选)文件里的骨架"),
            ),
        default = '各自骨架',
        )


    启用导入骨架添加T姿势: bpy.props.BoolProperty(
        name = "启用导入骨架添加T姿势",
        default = True,
        description = '', 
    )


    UpperArm展平: bpy.props.BoolProperty(
        name = "UpperArm展平",
        default = True,
        description = '', 
    )

    Clavicle展平: bpy.props.BoolProperty(
        name = "Clavicle展平",
        default = True,
        description = '', 
    )

    Hand展平: bpy.props.BoolProperty(
        name = "Hand展平",
        default = True,
        description = '', 
    )

    Finger0展平: bpy.props.BoolProperty(
        name = "Finger0展平",
        default = True,
        description = '', 
    )



class ZHUFILE_OT_骨架_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_armature"
    bl_label  = "选项设置"        

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        sets(self, context)
        operator = context.space_data.active_operator
        draw(self, operator.骨架)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ZHUFILE_PT_骨架_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_armature_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "骨架.选项设置"
    bl_options = {'INSTANCED'} # bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x = 13


    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import" # "zhufile.import" -> "ZHUFILE_OT_import"

    def draw(self, context):
        sets(self, context)
        operator = context.space_data.active_operator
        draw(self, operator.骨架)




def sets(self, context):
    operator = context.space_data.active_operator
    if operator.变换.坐标系变换模式 != "自动处理" or operator.旋转.坐标系旋转模式 != "自动处理":
        operator.骨架.UpperArm展平, operator.骨架.Clavicle展平 = False, False
        operator.骨架.Finger0展平, operator.骨架.Hand展平 = False, False


def draw(self, 骨架):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False
    # draw_坐标变换(layout, 骨架)
    box = layout.box()
    box.label(text="Blender Edit Bone 空间")
    draw_骨骼长度(box, 骨架)
    draw_合并骨架(box, 骨架)
    box = layout.box()
    draw_骨架伸展(box, 骨架)



def draw_骨骼长度(box, 骨架):
    box.prop(骨架, "骨骼长度处理模式")
    if 骨架.骨骼长度处理模式 == "手动设置": box.prop(骨架, "骨骼长度")


def draw_合并骨架(box, 骨架):
    box.label(text="无需导入骨架，请选【略过骨架】选项", icon='OBJECT_DATAMODE')
    box.prop(骨架, "骨架导入模式")
    if 骨架.骨架导入模式 == "合并的骨架":
        box.label(text="警告::会将所选的文件里所有的骨架全部合并！")
        box.label(text="请注意是否有，不想合并的模型！")
        box.label(text="一般与【选择集选项设置-所选范围扩展-自动推测】配合使用！")
    
def draw_骨架伸展(box, 骨架):
    box.use_property_split = False
    row = box.row()
    row.label(text="骨架添加T姿势"), row.prop(骨架, "启用导入骨架添加T姿势")
    if 骨架.启用导入骨架添加T姿势:
        row = box.row()
        row.prop(骨架, "UpperArm展平"), row.prop(骨架, "Clavicle展平")
        row = box.row()
        row.prop(骨架, "Finger0展平"), row.prop(骨架, "Hand展平")

        box.label(text="一般配合，骨架导入模式-合并骨架使用") # , icon='INFO')
        box.label(text="骨架转成T姿势之前，要求骨骼轴向进行坐标系变换") # , icon='INFO')
        box.label(text="故，坐标系变换模式、坐标系旋转模式都需设置为自动处理") # , icon='INFO')