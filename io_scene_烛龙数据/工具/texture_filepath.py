import os


def relpath_convert_abspath(filepath:str, *relpaths):
    dircwde = os.getcwd()
    dirname = os.path.dirname(filepath)
    os.chdir(dirname)

    abspaths = []
    relpaths = [relpath for relpath in relpaths if relpath !=""]
    for relpath in relpaths: abspaths.append(os.path.abspath(relpath))

    os.chdir(dircwde)
    
    if len(abspaths) == 1: return abspaths[0]
    return abspaths


# E:/Program_StructFiles/GuJianQT3/asset/characters/actress1/models/actress1_default_bodya.model
# Material #3991/<g3_cloth2>actress1_default_body
# ..\textures\actress1_default_body_01d.tga
# ..\textures\actress1_default_body_01s.tga
# ..\textures\actress1_default_body_01n.tga
# ..\textures\actress1_default_body_01m.tga
def 测试():
    dircwd = os.getcwd()
    filepathi = r"E:/Program_StructFiles/GuJianQT3/asset/characters/actress1/models/actress1_default_bodya.model"
    dirname = os.path.dirname(filepathi)
    os.chdir(dirname)
    relpath = r"..\textures\actress1_default_body_01d.tga"
    filepatho = os.path.abspath(relpath)
    os.chdir(dircwd)
    print(filepatho)

# filepathi = r"E:/Program_StructFiles/GuJianQT3/asset/characters/actress1/models/actress1_default_bodya.model"
# relpaths = [
# r"..\textures\actress1_default_body_01d.tga",
# r"..\textures\actress1_default_body_01s.tga",
# r"..\textures\actress1_default_body_01n.tga",
# r"..\textures\actress1_default_body_01m.tga",
# ]
# abspaths = relpath_convert_abspath(filepathi, *relpaths)
# print(abspaths)



# os.path.normpath(): 规范化路径
# os.path.getmtime(filepath): 获取最后修改时间
# os.path.getsize(filepath): 获取文件大小
# os.path.exists(filepath): 判断路径是否存在
# os.path.isfile(filepath): 判断是否为文件
# os.path.isdir(filepath): 判断是否为目录
# os.path.split(filepath): 分割目录和文件名
# os.path.basename(filepath): 获取文件名
# os.path.dirname(filepath): 获取目录名

# os.path.abspath(filepath): 获取绝对路径
# os.path.splitext(filepath): 分割文件名和扩展名

# os.getcwd( )：工作目录
# os.chdir( )：改变工作目录