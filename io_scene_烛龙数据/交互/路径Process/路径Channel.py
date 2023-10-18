
import os
import traceback

from ... import 数据, 接口, 文件, 工具





recent_collection_name = None
# 核心思路，把所选的每个文件都当成1个选择集
def 查询古剑123filename字典(filenames):
    global recent_collection_name

    模型列表, 动画列表, 选择集列表 = __文件路径__to__多列表__(filenames)

    collection_filenames_list = []

    for filename in 模型列表: 
        collection_name, result_filenames = __查询__模型字典__(filename)
        collection_filenames_list.append([collection_name, result_filenames])

    # 文件浏览器的导入功能，只支持在同一文件夹里多选，从而保证模型及动画以下的对应代码不出错
    for filename in 动画列表: 
        collection_name, result_filenames = __动画__选择集名称__(filename)
        collection_filenames_list.append([collection_name, result_filenames])
    recent_collection_name = None

    for filename in 选择集列表: 
        collection_name, result_filenames = __选择集__选择集名称__(filename)
        collection_filenames_list.append([collection_name, result_filenames])

    return collection_filenames_list



def __文件路径__to__多列表__(filenames):
    模型列表, 动画列表, 选择集列表 = [], [], []
    for filename in filenames: 
        match os.path.splitext(filename)[-1]:
            case ".fbx"   : 模型列表.append(filename)
            case ".nif"   : 模型列表.append(filename) 
            case ".kf"    : 动画列表.append(filename)
            case ".xac"   : 模型列表.append(filename)
            case ".xsm"   : 动画列表.append(filename)
            case ".vmesh" : 模型列表.append(filename)
            case ".model" : 模型列表.append(filename)
            case ".hka"   : 动画列表.append(filename)
            case ".hkx"   : 动画列表.append(filename)
            case ".avatar": 选择集列表.append(filename)
            case ".srt"   : 模型列表.append(filename)
            case     _    : 模型列表.append(filename)
    return 模型列表, 动画列表, 选择集列表



def __查询__模型字典__(filename):
    # print(os.path.splitext(filename)[-1])
    match os.path.splitext(filename)[-1]:
        case ".nif"   : return __查询__古剑1字典__(filename) 
        case ".xac"   : return __查询__古剑2字典__(filename)     
        case     _    : return __模型__选择集名称__(filename)

    
def __模型__选择集名称__(filename):
    # 未查到模型选择集名称的，模型文件是挂载到scene.collection.Collection
    return "Collection", [filename]
    

def __动画__选择集名称__(filename):
    collection_name = ""
    if recent_collection_name != None: collection_name = recent_collection_name
    # 单独的动画文件，也是需要是挂载的scene.collection，防止出现新建空Collection
    # 和模型一起选的动画文件，需要挂载到模型文件的的选择集
    return collection_name, [filename]


def __选择集__选择集名称__(filename):
    # 选择集文件是挂载的scene.collection，防止出现新建空Collection
    return "", [filename]






def __查询__古剑1字典__(filename):
    global recent_collection_name 
    # ".nif"
    if "古剑1" not in 数据.变量.选择.名称替换: return "Collection", [filename]
    if filename in 数据.常量.古剑1字典:
        collection_name = 数据.常量.古剑1字典[filename]
    else:
        collection_name = "Collection"
    recent_collection_name = collection_name
    return collection_name, [filename]


def __查询__古剑2字典__(filename):
    global recent_collection_name 
    # ".xac"
    if "古剑2" not in 数据.变量.选择.名称替换: return "Collection", [filename]
    if filename in 数据.常量.古剑2字典:
        collection_name, filenames = 数据.常量.古剑2字典[filename]
    else:
        collection_name, filenames = "Collection", [filename]
    recent_collection_name = collection_name
    return collection_name, filenames








def 合并选择集列表(filenames, collection_filenames_list):
    match 数据.变量.选择.所选范围扩展:
        case "自动推测": return __选项设置__所选范围扩展(collection_filenames_list)
        case "当前多选": return __选项设置__所选范围限定(filenames, collection_filenames_list)


def __选项设置__所选范围限定(filenames, collection_filenames_list):
    collection_filenames_dict = {}
    for collection_name, names in collection_filenames_list:
        collection_filenames_dict[collection_name] = []

    for [collection_name, names], filename in zip(collection_filenames_list, filenames): 
        if filename not in collection_filenames_dict[collection_name]: collection_filenames_dict[collection_name].append(filename)

    return collection_filenames_dict


def __选项设置__所选范围扩展(collection_filenames_list):
    collection_filenames_dict = {}
    for collection_name, filenames in collection_filenames_list: 
        collection_filenames_dict[collection_name] = []

    for collection_name, filenames in collection_filenames_list:
        for filename in filenames:
            if filename not in collection_filenames_dict[collection_name]: collection_filenames_dict[collection_name].append(filename)
    return collection_filenames_dict


def 新建选择集列表(directory, collection_filenames_dict):
    选择集列表 = []
    for collection_name, filenames in collection_filenames_dict.items():
        选择集 = 接口.标记.选择集()
        选择集.名称 = collection_name
        选择集.filepaths = [directory+filename for filename in filenames]
        选择集列表.append(选择集)
    return 选择集列表












