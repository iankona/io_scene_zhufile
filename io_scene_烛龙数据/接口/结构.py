


class 插件材质:
    def __init__(self):
        self.filepath = ""
        self.名称 = ""
        self.标签贴图相对地址列表 = []
        self.标签贴图绝对地址列表 = []

        self.基础色 = (0.0, 0.0, 0.0, 1)       # ["Base Color"]
        self.次表面 = 0.0                      # ["Subsurface"]
        self.次表面半径 = [1.0, 0.2, 0.1]      # ["Subsurface Radius"]
        self.次表面颜色 =  (1.0, 1.0, 1.0, 1)  # ["Subsurface Color"]
        self.次表面IOR = 0.0                   # ["Subsurface IOR"]
        self.次表面各向异性 = 0.0              # ["Subsurface Anisotropy"]
        self.金属度 = 0.0                      # ["Metallic"]
        self.高光 = 0.0                        # ["Specular"]
        self.高光染色 = 0.0                    # ["Specular Tint"]
        self.糙度 = 0.0                        # ["Roughness"]
        self.各向异性过滤 = 0.0                # ["Anisotropic"]
        self.各向异性旋转 = 0.0                # ["Anisotropic Rotation"]
        self.光泽 = 0.0                        # ["Sheen"]
        self.光泽染色 = 0.0                    # ["Sheen Tint"]
        self.清漆 = 0.0                        # ["Clearcoat"]
        self.清漆粗糙度 = 0.0                  # ["Clearcoat Roughness"]
        self.IOR折射率 = 0.0                   # ["IOR"]
        self.透射 = 0.0                        # ["Transmission"]
        self.透射粗糙度 = 0.0                  # ["Transmission Roughness"]
        self.自发光 = (0.0, 0.0, 0.0, 1)       # ["Emission"]
        self.自发光强度 = 0.0                  # ["Emission Strength"]
        self.透明 = 1.0                        # ["Alpha"]
        self.法向 = None                       # ["Normal"]
        self.清漆法向 = None                   # ["Clearcoat Normal"]
        self.切向正切 = None                   # ["Tangent"]


class 插件网格:
    def __init__(self):
        self.骨骼组列表 = [] # 文件数据, [ [[boneid, value], [boneid, value],],  [[boneid, value], [boneid, value],], ]

        self.名称 = "" # 只有古剑1的nif有网格名称，其他为空值
        self.插件材质 = 插件材质() # 保证没有UV的网格，也能有材质，贴图列表可为空列表
        self.顶点列表 = []   # mathutils.Vector([x,y,z])
        self.顶点UV列表 = [] # [[u,v],...]
        self.顶点Loop列表 = []
        self.顶点组字典 = {} # 插件数据, [ [bonename, [[vertid, value], [vertid, value],,,]], ] # 注意boneid 需转换为bonename
        self.形态键列表 = [] # [[形态名称, [Vector(x,y,z), ...]]]


class 文件骨架:
    class 骨骼:
        def __init__(self):
            self.name = ""
            self.parentname = ""
            self.matrix_local = None # mathutils.Matrix() # 4x4

            self.location = None # 坐标变换，旋转变换，缩放变换 # mathutils.Vector([vx, vy, vz])
            self.rotation_quaternion = None # 骨骼轴向变换 # mathutils.Quaternion([qw, qx, qy, qz])
            self.scale = None # mathutils.Vector([vx, vy, vz])


    def __init__(self):
        self.骨骼字典 = {}


class 插件骨架:
    class 骨骼:
        def __init__(self):
            self.name = ""
            self.parent = None
            self.children = []

            self.head = None # mathutils.Vector([vx, vy, vz])
            self.tail = None # mathutils.Vector([vx, vy, vz])
            self.roll = None # double
            self.length = None 

    def __init__(self):
        self.骨骼字典 = {}


class 文件姿态: # 骨骼空间
    class 骨骼:
        def __init__(self):
            self.名称 = ""
            self.位置帧列表 = [] # 规定[frame, bone_location],   frame需在前
            self.旋转帧列表 = [] # 规定[frame, bone_quaternion], frame需在前
            self.缩放帧列表 = [] # 规定[frame, bone_scale],      frame需在前


    def __init__(self):
        self.骨骼字典 = {}


class 插件姿态: # 相对空间
    class 骨骼:
        def __init__(self):
            self.名称 = ""
            self.位置帧列表 = [] # 规定[frame, basis_location],   frame需在前
            self.旋转帧列表 = [] # 规定[frame, basis_quaternion], frame需在前
            self.缩放帧列表 = [] # 规定[frame, basis_scale],      frame需在前


    def __init__(self):
        self.骨骼字典 = {}