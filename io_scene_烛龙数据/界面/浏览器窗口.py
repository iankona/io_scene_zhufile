import bpy

from .. import 交互, 数据
from .  import 面板


class ZHUFILE_OT_加载(bpy.types.Operator):
    """    古剑奇谭：琴心剑魄今何在，
    古剑奇谭二：永夜初晗凝碧天，
    古剑奇谭三：梦付千秋星垂野。"""
    # 静态属性
    bl_idname = "zhufile.import"  # -> ZHUFILE_OT_import, Blender28界面UI按钮和菜单项绑定本类的唯一标识符。有规范，而且不能和类定义名称重叠
    bl_label = "加载"                    # 弹出的文件浏览器的确定按钮上显示的文本
    bl_options = {'PRESET', 'UNDO'}
    
    # 实例属性
    # filter_glob: bpy.props.StringProperty(
    #     default="*.obj;*.mtl",
    #     options={'HIDDEN'},
    #     )

    # filepath: bpy.props.StringProperty(
    #     name = "File Path",
    #     description = "Filepath used for importing the file",
    #     maxlen = 1024,
    #     subtype = 'FILE_PATH',
    # )

    # files是固定名称，改成filenames等变量名称，则接收不到filenames
    files: bpy.props.CollectionProperty(
        type = bpy.types.PropertyGroup,
        )
    UI类型: bpy.props.PointerProperty(type=面板.UI类型.ZHUFILE_PROP_UI组)

    选择: bpy.props.PointerProperty(type=面板.选择.ZHUFILE_PROP_UI组)
    
    材质: bpy.props.PointerProperty(type=面板.材质.ZHUFILE_PROP_UI组)
    UV: bpy.props.PointerProperty(type=面板.UV.ZHUFILE_PROP_UI组)
    贴图: bpy.props.PointerProperty(type=面板.贴图.ZHUFILE_PROP_UI组)

    变换: bpy.props.PointerProperty(type=面板.变换.ZHUFILE_PROP_UI组) # 需要先注册UI组，在注册本类，否则会出现Operator不支持此类别注册的错误
    旋转: bpy.props.PointerProperty(type=面板.旋转.ZHUFILE_PROP_UI组)
    网格: bpy.props.PointerProperty(type=面板.网格.ZHUFILE_PROP_UI组)
    骨架: bpy.props.PointerProperty(type=面板.骨架.ZHUFILE_PROP_UI组)
    姿态: bpy.props.PointerProperty(type=面板.姿态.ZHUFILE_PROP_UI组)
    姿态通道位置: bpy.props.PointerProperty(type=面板.姿态通道位置.ZHUFILE_PROP_UI组)
    姿态通道旋转: bpy.props.PointerProperty(type=面板.姿态通道旋转.ZHUFILE_PROP_UI组)
    姿态通道缩放: bpy.props.PointerProperty(type=面板.姿态通道缩放.ZHUFILE_PROP_UI组)        

    古剑1选项: bpy.props.PointerProperty(type=面板.古剑1选项.ZHUFILE_PROP_UI组)
    古剑2选项: bpy.props.PointerProperty(type=面板.古剑2选项.ZHUFILE_PROP_UI组)
    古剑3选项: bpy.props.PointerProperty(type=面板.古剑3选项.ZHUFILE_PROP_UI组)
    def execute(self, context):
        交互.加载Lanuch.函数(directory=self.directory, filegroups=self.files)
        return {'FINISHED'}


    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


    def draw(self, context):
        self.directory = bpy.context.space_data.params.directory.decode() # 放到execute(self, context)函数里，出现：AttributeError: 'Space' object has no attribute 'params'
        数据.变量.UI类型 = self.UI类型

        数据.变量.选择 = self.选择

        数据.变量.材质 = self.材质
        数据.变量.UV = self.UV
        数据.变量.贴图 = self.贴图

        数据.变量.变换 = self.变换
        数据.变量.旋转 = self.旋转
        数据.变量.骨架 = self.骨架
        数据.变量.网格 = self.网格

        数据.变量.姿态 = self.姿态
        数据.变量.姿态通道位置 = self.姿态通道位置
        数据.变量.姿态通道旋转 = self.姿态通道旋转
        数据.变量.姿态通道缩放 = self.姿态通道缩放

        数据.变量.古剑1选项 = self.古剑1选项
        数据.变量.古剑2选项 = self.古剑2选项
        数据.变量.古剑3选项 = self.古剑3选项
        pass
        # 关闭浏览器显示属性功能，以便交给面板显示


class ZHUFILE_OT_保存(bpy.types.Operator):
    """    古剑奇谭：琴心剑魄今何在,
    古剑奇谭二：永夜初晗凝碧天,
    古剑奇谭三：梦付千秋星垂野。"""

    bl_idname = "zhufile.export"  # -> ZHUFILE_OT_export
    bl_label  = "保存"           
    bl_options = {'PRESET', 'UNDO'}

    # 实例属性
    # filter_glob: bpy.props.StringProperty(
    #     default="*.obj;*.mtl",
    #     options={'HIDDEN'},
    #     )

    # filepath: bpy.props.StringProperty(
    #     name = "File Path",
    #     description = "Filepath used for importing the file",
    #     maxlen = 1024,
    #     subtype = 'FILE_PATH',
    # )

    # files是固定名称，改成filenames等变量名称，则接收不到filenames
    files: bpy.props.CollectionProperty(
        type = bpy.types.PropertyGroup,
        )

    def execute(self, context):
        self.report({'INFO'}, "%s" % "保存弹窗有执行")
        # pass
        return {'FINISHED'}


    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}





