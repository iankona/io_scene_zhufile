from ... import 接口


class struct:
    def __init__(self):
        self.filepath = ""
        self.材质字典 = {}
        self.文件骨架 = None
        self.插件网格列表 = []
        self.文件姿态 = None
        self.选择集列表 = []


    def struct_to_插件数据(self, 选择集):
        插件数据 = 接口.标记.插件数据()
        插件数据.filepath = self.filepath
        插件数据.文件骨架 = self.文件骨架
        for 插件网格 in self.插件网格列表: # 材质要求必须要有，贴图列表可以为[]
            插件网格.插件材质.filepath = self.filepath
        插件数据.插件网格列表 = self.插件网格列表
        插件数据.文件姿态 = self.文件姿态
        插件数据.选择集列表 = self.选择集列表
        for 材质名称, 插件材质 in self.材质字典.items(): 
            插件材质.filepath = self.filepath
            选择集.材质字典[材质名称] = 插件材质
        选择集.插件数据列表.append(插件数据)
 
        
