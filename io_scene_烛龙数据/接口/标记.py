

class 插件数据:
    def __init__(self):
        self.filepath = ""

        self.文件骨架 = None
        self.插件骨架 = None
        self.软件armatureobj = None

        self.插件网格列表 = []
        self.软件materials = []
        self.软件meshs = []
        self.软件objects = []

        self.文件姿态 = None # bone space
        # self.插件姿态 = None # basis space # 与选择的armature高度绑定，单独处理
        # self.软件action = None # 与选择的armature高度绑定，单独处理

        self.选择集列表 = []


class 选择集:
    def __init__(self):
        self.filepaths = []
        self.filedatas = []
        self.材质字典 = {}
        self.插件数据列表 = []

        self.armaturepath = None
        self.插件骨架 = None
        self.软件armatureobj = None

        self.actionpath = None
        self.文件姿态 = None

        self.名称 = ""
        self.软件collection = None


