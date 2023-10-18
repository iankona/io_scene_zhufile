import os
import bpy

from . import 浏览器窗口
from . import 面板
from . import 其他面板
from . import 面板组织
from . import 其他面板组织


类列表 = [
    面板.UI类型.ZHUFILE_PROP_UI组,
    面板.UI类型.ZHUFILE_PT_UI类型,

    面板.选择.ZHUFILE_OT_选择_选项设置,
    
    面板.材质.ZHUFILE_OT_材质_选项设置,
    面板.UV.ZHUFILE_OT_UV_选项设置,
    面板.贴图.ZHUFILE_OT_贴图_选项设置,

    面板.变换.ZHUFILE_OT_变换_选项设置,
    面板.旋转.ZHUFILE_OT_旋转_选项设置,
    面板.骨架.ZHUFILE_OT_骨架_选项设置,
    面板.网格.ZHUFILE_OT_网格_选项设置,
    面板.姿态.ZHUFILE_OT_姿态_选项设置,
    面板.姿态通道位置.ZHUFILE_OT_姿态通道位置_选项设置,
    面板.姿态通道旋转.ZHUFILE_OT_姿态通道旋转_选项设置,
    面板.姿态通道缩放.ZHUFILE_OT_姿态通道缩放_选项设置,


    面板.选择.ZHUFILE_PROP_UI组,

    面板.材质.ZHUFILE_PROP_UI组,
    面板.UV.ZHUFILE_PROP_UI组,
    面板.贴图.ZHUFILE_PROP_UI组,

    面板.变换.ZHUFILE_PROP_UI组,
    面板.旋转.ZHUFILE_PROP_UI组,
    面板.网格.ZHUFILE_PROP_UI组,
    面板.骨架.ZHUFILE_PROP_UI组,
    面板.姿态.ZHUFILE_PROP_UI组,
    面板.姿态通道位置.ZHUFILE_PROP_UI组,
    面板.姿态通道旋转.ZHUFILE_PROP_UI组,
    面板.姿态通道缩放.ZHUFILE_PROP_UI组,   

    面板.古剑1选项.ZHUFILE_PROP_UI组,
    面板.古剑2选项.ZHUFILE_PROP_UI组,
    面板.古剑3选项.ZHUFILE_PROP_UI组,

    面板.选择.ZHUFILE_PT_选择_选项设置,

    面板.材质.ZHUFILE_PT_材质_选项设置,
    面板.UV.ZHUFILE_PT_UV_选项设置,
    面板.贴图.ZHUFILE_PT_贴图_选项设置,

    面板.变换.ZHUFILE_PT_变换_选项设置,
    面板.旋转.ZHUFILE_PT_旋转_选项设置,
    面板.骨架.ZHUFILE_PT_骨架_选项设置,
    面板.网格.ZHUFILE_PT_网格_选项设置,
    面板.姿态.ZHUFILE_PT_姿态_选项设置,
    面板.姿态通道位置.ZHUFILE_PT_姿态通道位置_选项设置,
    面板.姿态通道旋转.ZHUFILE_PT_姿态通道旋转_选项设置,
    面板.姿态通道缩放.ZHUFILE_PT_姿态通道缩放_选项设置,


    面板组织.ZHUFILE_PT_选择集,

    面板组织.ZHUFILE_PT_材质,
    面板组织.ZHUFILE_PT_UV,
    面板组织.ZHUFILE_PT_贴图,

    面板组织.ZHUFILE_PT_变换,
    面板组织.ZHUFILE_PT_旋转,  
    面板组织.ZHUFILE_PT_骨架, 
    面板组织.ZHUFILE_PT_网格,       
    面板组织.ZHUFILE_PT_姿态, 
    面板组织.ZHUFILE_PT_姿态通道位置, 
    面板组织.ZHUFILE_PT_姿态通道旋转, 
    面板组织.ZHUFILE_PT_姿态通道缩放,        


    面板组织.ZHUFILE_PT_其他设置,    
    面板.古剑1选项.ZHUFILE_PT_古剑1选项,
    面板.古剑2选项.ZHUFILE_PT_古剑2选项,
    面板.古剑3选项.ZHUFILE_PT_古剑3选项,

    浏览器窗口.ZHUFILE_OT_加载,
    # 浏览器窗口.ZHUFILE_OT_保存,
]


其他类列表 = [
    其他面板组织.ZHUFILE_PT_其他功能,  
    其他面板组织.ZHUFILE_PT_贴图_批量转换, 
    其他面板组织.ZHUFILE_PT_骨架_切换动作, 

    其他面板.贴图批量转换.ZHUFILE_PROP_DDS组,
    其他面板.贴图批量转换.ZHUFILE_PROP_PNG组,
    其他面板.贴图批量转换.ZHUFILE_PROP_文件,
    其他面板.贴图批量转换.ZHUFILE_UL_选择文件列表,
    其他面板.贴图批量转换.ZHUFILE_UL_保存文件列表,

    其他面板.骨架切换动作.ZHUFILE_PROP_骨架,
    其他面板.骨架切换动作.ZHUFILE_PROP_动作,
    其他面板.骨架切换动作.ZHUFILE_UL_选择骨架列表,
    其他面板.骨架切换动作.ZHUFILE_UL_骨架动作列表,
    其他面板.骨架切换动作.ZHUFILE_PROP_骨架展平组,

    其他面板.插件全局变量.ZHUFILE_插件首选项,

    其他面板.贴图批量转换.ZHUFILE_OT_贴图_批量转换_添加函数,
    其他面板.贴图批量转换.ZHUFILE_OT_贴图_批量转换_转换函数,
    其他面板.贴图批量转换.ZHUFILE_OT_贴图_批量转换_清空函数,

    其他面板.贴图批量转换.ZHUFILE_OT_贴图_批量转换_选项设置, 
    其他面板.贴图批量转换.ZHUFILE_PT_贴图_批量转换_选项设置,


    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_添加函数,
    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_更换函数,
    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_删除函数,
    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_清空函数,
    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_古剑1添加T姿势函数,
    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_古剑2添加T姿势函数,
    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_古剑3添加T姿势函数,
    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_姿势复位函数,

    其他面板.骨架切换动作.ZHUFILE_OT_骨架_切换动作_选项设置,
    其他面板.骨架切换动作.ZHUFILE_PT_骨架_切换动作_选项设置,

]


def 新建菜单栏_导入(self, context):
    self.layout.operator(浏览器窗口.ZHUFILE_OT_加载.bl_idname, text = "烛龙数据 (.model/.xac/.nif/.xsm......)")


def 新建菜单栏_导出(self, context):
    self.layout.operator(浏览器窗口.ZHUFILE_OT_保存.bl_idname, text = "烛龙数据 (.model/.xml......)")


def 注册函数():
    os.system("CHCP 65001")

    # 注册类
    列表 = 类列表 + 其他类列表
    for 类 in 列表: bpy.utils.register_class(类)

    # 注册菜单栏():
    bpy.types.TOPBAR_MT_file_import.append(新建菜单栏_导入)
    # bpy.types.TOPBAR_MT_file_export.append(新建菜单栏_导出)


def 取消函数():
    # 取消类
    列表 = 类列表 + 其他类列表
    for 类 in 列表[::-1]: bpy.utils.unregister_class(类)

    # 取消菜单栏():
    bpy.types.TOPBAR_MT_file_import.remove(新建菜单栏_导入)
    # bpy.types.TOPBAR_MT_file_export.remove(新建菜单栏_导出)