

bl_info = {
    "name": "烛龙数据",
    "author": "AnsWdy ShaWa",
    "version": (2, 6, 4),
    "blender": (3, 3, 0),
    "location": "File > Import-Export",
    "description": "nif, kf, xac, xsm, vmesh, avatar, model, hkx, hka等游戏数据文件加载插件",
    "warning": "",
    "doc_url": "/addons/测试/文档.md", # {BLENDER_MANUAL_URL}
    "support": 'OFFICIAL',
    "category": "Import-Export",
    }


from . import 界面


# 程序启动时执行
# 插件管理界面勾选插件时执行
def register(): 界面.注册.注册函数()


# 插件管理界面取消勾选插件时执行
def unregister(): 界面.注册.取消函数()


