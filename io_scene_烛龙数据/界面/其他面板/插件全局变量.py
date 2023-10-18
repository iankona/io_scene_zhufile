import bpy
from . import 贴图批量转换
from . import 骨架切换动作


class ZHUFILE_插件首选项(bpy.types.AddonPreferences): # 插件首选项，插件全局设置
    bl_idname = "io_scene_烛龙数据"

    dds: bpy.props.PointerProperty(type=贴图批量转换.ZHUFILE_PROP_DDS组)
    png: bpy.props.PointerProperty(type=贴图批量转换.ZHUFILE_PROP_PNG组)
    选择集索引: bpy.props.IntProperty(name="选择集索引", default=0)
    选择文件组: bpy.props.CollectionProperty(type=贴图批量转换.ZHUFILE_PROP_文件)
    保存集索引: bpy.props.IntProperty(name="保存集索引", default=0)
    保存文件组: bpy.props.CollectionProperty(type=贴图批量转换.ZHUFILE_PROP_文件)

    # 所选骨架组: bpy.props.CollectionProperty(type=bpy.types.Object)
    # 骨架动作组: bpy.props.CollectionProperty(type=bpy.types.Action)
    # # ValueError: bpy_struct "ZHUFILE_插件首选项" registration error: '所选骨架组' CollectionProperty could not register because this type doesn't support data-block properties

    骨架集索引: bpy.props.IntProperty(name="骨架集索引", default=0)
    选择骨架组: bpy.props.CollectionProperty(type=骨架切换动作.ZHUFILE_PROP_骨架)
    动作集索引: bpy.props.IntProperty(name="动作集索引", default=0)
    骨架动作组: bpy.props.CollectionProperty(type=骨架切换动作.ZHUFILE_PROP_动作)

    骨架展平: bpy.props.PointerProperty(type=骨架切换动作.ZHUFILE_PROP_骨架展平组)
    def draw(self, context):
        pass