import os

import bpy
import math
import mathutils



class ZHUFILE_PROP_骨架展平组(bpy.types.PropertyGroup):
    启用当前帧变为T姿势: bpy.props.BoolProperty(
        name = "启用当前帧变为T姿势",
        default = False,
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



class ZHUFILE_PROP_骨架(bpy.types.PropertyGroup): 
    name: bpy.props.StringProperty(
        name="name",
        description="骨架名称",
        default="未命名")


class ZHUFILE_PROP_动作(bpy.types.PropertyGroup): 
    name: bpy.props.StringProperty(
        name="name",
        description="动作名称",
        default="未命名")
    
    armature_name: bpy.props.StringProperty(
        name="armature_name",
        description="骨架名称",
        default="未命名")


class ZHUFILE_UL_选择骨架列表(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon='OBJECT_DATAMODE')

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='OBJECT_DATAMODE')


class ZHUFILE_UL_骨架动作列表(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon='OBJECT_DATAMODE')

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon='OBJECT_DATAMODE')


class ZHUFILE_OT_骨架_切换动作_添加函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_add_armature"
    bl_label  = "添加所选骨架" 
    # print(bpy.context.space_data.params.files) # AttributeError: 'FileSelectParams' object has no attribute 'files'
    # operator: bpy.props.PointerProperty(type=bpy.types.PropertyGroup) # AttributeError: bpy_struct: attribute "operator" from "ZHUFILE_OT_func_add_texture_batch_convert" is read-only
    def execute(self, context):
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.选择骨架组.clear()
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.骨架动作组.clear()
        __添加骨架函数__()
        __添加动作函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}

def __添加骨架函数__():
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    for object in bpy.context.selected_objects:
        if object.type != "ARMATURE": continue
        # is_in_group = False
        # for armatureprop in addon_prefs.选择骨架组:
        #     if armatureprop.name == object.name:
        #         is_in_group = True
        #         break
        # if is_in_group: continue
        armatureprop = addon_prefs.选择骨架组.add()
        armatureprop.name = object.name



def __添加动作函数__():
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    for armatureprop in addon_prefs.选择骨架组:
        for action in bpy.data.actions:
            if armatureprop.name not in action.name: continue
            # is_in_group = False
            # for actionprop in addon_prefs.骨架动作组:
            #     if actionprop.name == action.name:
            #         is_in_group = True
            #         break
            # if is_in_group: continue
            actionprop = addon_prefs.骨架动作组.add()
            actionprop.name = action.name
            actionprop.armature_name = armatureprop.name


class ZHUFILE_OT_骨架_切换动作_更换函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_switch_action"
    bl_label  = "转换函数" 
    def execute(self, context):
        __更换动作函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)


def __更换动作函数__():
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    action_prop = addon_prefs.骨架动作组[addon_prefs.动作集索引]
    armatureobj = bpy.data.objects[action_prop.armature_name]
    action = bpy.data.actions[action_prop.name]
    armatureobj.animation_data_clear()
    armatureobj.animation_data_create()
    armatureobj.animation_data.action = action
    # addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    # if len(addon_prefs.骨架动作组) == 0: return None
    # armature_prop = addon_prefs.选择骨架组[addon_prefs.骨架集索引]
    # action_prop = addon_prefs.骨架动作组[addon_prefs.动作集索引]
    # armatureobj = bpy.data.objects[armature_prop.name]
    # action = bpy.data.actions[action_prop.name]
    # armatureobj.animation_data_clear()
    # armatureobj.animation_data_create()
    # armatureobj.animation_data.action = action



class ZHUFILE_OT_骨架_切换动作_删除函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_remove_action"
    bl_label  = "删除函数" 
    def execute(self, context):
        __删除所选动作__()
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.选择骨架组.clear()
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.骨架动作组.clear()
        __添加骨架函数__()
        __添加动作函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)

def __删除所选动作__():
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    action_prop = addon_prefs.骨架动作组[addon_prefs.动作集索引]
    action = bpy.data.actions[action_prop.name]
    for object in bpy.context.selected_objects: # 删除action后，骨架并不会复位到原始姿态
        if object.type != "ARMATURE": continue
        if object.animation_data.action == action: object.animation_data_clear()
        __姿势复位__()
    # bpy.data.actions.remove(action_prop.name) # TypeError: BlendDataActions.remove(): error with argument 1, "action" -  Function.action expected a Action type, not str
    bpy.data.actions.remove(action)
    # addon_prefs.骨架动作组.remove(action_prop) # TypeError: bpy_prop_collection.remove(): expected one int argument
    addon_prefs.骨架动作组.remove(addon_prefs.动作集索引)
    addon_prefs.动作集索引 = 0





class ZHUFILE_OT_骨架_切换动作_清空函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_clear"
    bl_label  = "清空函数" 
    def execute(self, context):
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.选择骨架组.clear()
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.骨架动作组.clear()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)


class ZHUFILE_OT_骨架_切换动作_古剑1添加T姿势函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_gu1_add_tpose"
    bl_label  = "古剑1添加T姿势" 
    def execute(self, context):
        __古剑3添加T姿势函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)
    
class ZHUFILE_OT_骨架_切换动作_古剑2添加T姿势函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_gu2_add_tpose"
    bl_label  = "古剑2添加T姿势" 
    def execute(self, context):
        __古剑2添加T姿势函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)

class ZHUFILE_OT_骨架_切换动作_古剑3添加T姿势函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_gu3_add_tpose"
    bl_label  = "古剑3添加T姿势" 
    def execute(self, context):
        __古剑3添加T姿势函数__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)


def __古剑2添加T姿势函数__():
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    for object in bpy.context.selected_objects:
        if object.type != "ARMATURE": continue
        if addon_prefs.骨架展平.启用当前帧变为T姿势:
            frame_current = bpy.context.scene.frame_current
            __姿势复位__()
            __古剑2__设置T姿势__(addon_prefs, object, frame_current)
        else:
            object.animation_data_create()
            object.animation_data.action = bpy.data.actions.new(object.name+"_T_pose")
            bpy.context.scene.frame_current = 0
            __姿势复位__()
            __古剑2__设置T姿势__(addon_prefs, object, 0)

    if addon_prefs.骨架展平.启用当前帧变为T姿势:
        pass
    else:
        addon_prefs.选择骨架组.clear()
        addon_prefs.骨架动作组.clear()
        __添加骨架函数__()
        __添加动作函数__()


def __古剑3添加T姿势函数__():
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    for object in bpy.context.selected_objects:
        if object.type != "ARMATURE": continue
        if addon_prefs.骨架展平.启用当前帧变为T姿势:
            frame_current = bpy.context.scene.frame_current
            __姿势复位__()
            __古剑3__设置T姿势__(addon_prefs, object, frame_current)
        else:
            object.animation_data_create()
            object.animation_data.action = bpy.data.actions.new(object.name+"_T_pose")
            bpy.context.scene.frame_current = 0
            __姿势复位__()
            __古剑3__设置T姿势__(addon_prefs, object, 0)

    if addon_prefs.骨架展平.启用当前帧变为T姿势:
        pass
    else:
        addon_prefs.选择骨架组.clear()
        addon_prefs.骨架动作组.clear()
        __添加骨架函数__()
        __添加动作函数__()


def __古剑2__设置T姿势__(addon_prefs, 软件armatureobj, frame_current):
    for pbone in 软件armatureobj.pose.bones:
        for chars in ["UpperArm", "UpArmTwist"]:
            if chars in pbone.name and addon_prefs.骨架展平.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                euler = mathutils.Euler([0, 0, -z_rad], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)

        for chars in ["ForeTwist", "Forearm", "Finger01", "Finger02", "Finger01Nub", "Finger1", "Finger2", "Finger3", "Finger4"]:
            if chars in pbone.name and addon_prefs.骨架展平.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                # print(pbone.name, x_angle, y_angle, z_angle) # print(math.radians(90)) # 1.5707963267948966
                euler = mathutils.Euler([-x_rad, 0, 0], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)


        for chars in ["Hand"]:
            if chars in pbone.name and addon_prefs.骨架展平.Hand展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([0, vy, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)


        if pbone.name == "Bip01 R Finger0" or pbone.name == "Bip01 L Finger0":
            if addon_prefs.骨架展平.Finger0展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, vy, 0]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)


        for chars in ["Clavicle"]:  
            if chars in pbone.name and addon_prefs.骨架展平.Clavicle展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, 0, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)


def __古剑3__设置T姿势__(addon_prefs, 软件armatureobj, frame_current):
    for pbone in 软件armatureobj.pose.bones:
        for chars in ["UpperArm", "uparm"]:
            if chars in pbone.name and addon_prefs.骨架展平.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                # print(pbone.name, x_angle, y_angle, z_angle) # print(math.radians(90)) # 1.5707963267948966
                euler = mathutils.Euler([-x_rad, 0, 0], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)

        for chars in ["ForeTwist", "Forearm", "Finger01", "Finger02", "Finger01Nub", "Finger1", "Finger2", "Finger3", "Finger4"]:
            if chars in pbone.name and addon_prefs.骨架展平.UpperArm展平:
                x_rad, y_rad, z_rad = pbone.bone.matrix.to_euler()
                x_angle, y_angle, z_angle = math.degrees(x_rad), math.degrees(y_rad), math.degrees(z_rad)
                # print(pbone.name, x_angle, y_angle, z_angle) # print(math.radians(90)) # 1.5707963267948966
                euler = mathutils.Euler([0, 0, -z_rad], 'XYZ')
                pbone.rotation_quaternion = euler.to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)


        for chars in ["Hand"]:
            if chars in pbone.name and addon_prefs.骨架展平.Hand展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, vy, 0]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)


        if pbone.name == "Bip01 R Finger0" or pbone.name == "Bip01 L Finger0":
            if addon_prefs.骨架展平.Finger0展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([0, vy, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)


        for chars in ["Clavicle"]:
            if chars in pbone.name and addon_prefs.骨架展平.Clavicle展平:
                direct_local, roll_local = bpy.types.Bone.AxisRollFromMatrix(pbone.bone.matrix)
                # print(pbone.name, direct_local, roll_local)
                vx, vy, vz = direct_local
                matrix = bpy.types.Bone.MatrixFromAxisRoll(mathutils.Vector([vx, 0, vz]), roll_local)
                pbone.rotation_quaternion = (pbone.bone.matrix.inverted() @ matrix).to_quaternion()
                pbone.keyframe_insert("rotation_quaternion", frame=frame_current)




class ZHUFILE_OT_骨架_切换动作_姿势复位函数(bpy.types.Operator):
    bl_idname = "zhufile.func_switch_action_reset_pose"
    bl_label  = "姿势复位函数" 
    def execute(self, context):
        for object in bpy.context.selected_objects:
            if object.type != "ARMATURE": continue
            object.animation_data_clear()
            __姿势复位__()
        return {'FINISHED'}
    def draw(self, context):
        pass
    def invoke(self, context, event):
        return self.execute(context)
    

def __姿势复位__():
    bpy.ops.object.mode_set(mode="POSE")
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.transforms_clear()
    # bpy.ops.object.mode_set(mode="OBJECT")




class ZHUFILE_OT_骨架_切换动作_选项设置(bpy.types.Operator):
    bl_idname = "zhufile.property_armature_switch_action" # -> ZHUFILE_OT_property_...
    bl_label  = "选项设置" 

    def execute(self, context):
        # print("OK有运行")
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.选择骨架组.clear()
        bpy.context.preferences.addons["io_scene_烛龙数据"].preferences.骨架动作组.clear()
        return {'FINISHED'}
    def draw(self, context):
        draw(self)
        
    def invoke(self, context, event):
        context.window_manager.invoke_props_dialog(self, width=500)
        return {'RUNNING_MODAL'}


class ZHUFILE_PT_骨架_切换动作_选项设置(bpy.types.Panel):
    bl_idname = "FILEBROWSER_PT_zhufile_armature_switch_action_property"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "骨架切换动作.选项设置" # 不能删除
    bl_options = {'INSTANCED'}
    bl_ui_units_x = 25

    @classmethod
    def poll(cls, context):
        operator = context.space_data.active_operator
        return operator.bl_idname == "ZHUFILE_OT_import"

    def draw(self, context):
        draw(self)
        # operator = layout.operator("ZHUFILE_OT_property_texture_batch_convert", text="骨架切换动作弹窗") # <bpy_struct, ZHUFILE_OT_property_texture_batch_convert at 0x000002D376A62FC8>
        # operator = bpy.ops.zhufile.property_texture_batch_convert # <function bpy.ops.zhufile.property_texture_batch_convert at 0x1d5a962acb0'>


def draw(self):
    layout = self.layout
    addon_prefs = bpy.context.preferences.addons["io_scene_烛龙数据"].preferences
    operator = addon_prefs

    layout.label(text="切换所选骨架动作")
    row = layout.row()
    col = row.column()
    col.operator("ZHUFILE_OT_func_switch_action_add_armature", text="添加所选骨架")
    col.template_list("ZHUFILE_UL_选择骨架列表", "", operator, "选择骨架组", operator, "骨架集索引") # operator = self [operator, "选择集索引"] == operator.选择集索引
    col.operator("ZHUFILE_OT_func_switch_action_remove_action", text="删除所选动作")

    col = row.column()
    col.operator("ZHUFILE_OT_func_switch_action_switch_action", text="切换所选动作")
    col.template_list("ZHUFILE_UL_骨架动作列表", "", operator, "骨架动作组", operator, "动作集索引") # 后面测试下operator改bpy.types.PropertyGroup是否可行，以及如何让operator一直存在不被销毁，以及再draw之外能否新建实例
    col.operator("ZHUFILE_OT_func_switch_action_clear", text="清空列表")

    layout.separator()

    row = layout.row()
    row.label(text="所选骨架添加T姿势"), row.prop(addon_prefs.骨架展平, "启用当前帧变为T姿势")
    box = layout.box()
    box.use_property_split = False
    row = box.row()
    row.prop(addon_prefs.骨架展平, "UpperArm展平"), row.prop(addon_prefs.骨架展平, "Clavicle展平")
    row = box.row()
    row.prop(addon_prefs.骨架展平, "Finger0展平"),  row.prop(addon_prefs.骨架展平, "Hand展平")
    box.label(text="要求是经过坐标系变换自动处理、坐标系旋转自动处理的骨架") # , icon='INFO')
    row = layout.row()
    row.operator("ZHUFILE_OT_func_switch_action_gu1_add_tpose", text="古剑1添加T姿势")
    row.operator("ZHUFILE_OT_func_switch_action_gu2_add_tpose", text="古剑2添加T姿势")
    row.operator("ZHUFILE_OT_func_switch_action_gu3_add_tpose", text="古剑3添加T姿势")
    row = layout.row()
    row.operator("ZHUFILE_OT_func_switch_action_reset_pose", text="恢复原始姿势")
    
 