import os


from ... import 数据, 工具




def 贴图处理():
    for 插件名称, 插件材质 in 数据.变量.选择集.材质字典.items(): __贴图格式处理__(插件材质)
    for 插件数据 in 数据.变量.选择集.插件数据列表:
        for 插件网格 in 插件数据.插件网格列表:
            __贴图路径处理__(插件数据.filepath, 插件网格.插件材质)
            __贴图格式处理__(插件网格.插件材质)


def __贴图路径处理__(filepath, 插件材质):
    for 标签, 相对贴图地址 in 插件材质.标签贴图相对地址列表:
        绝对贴图地址 = 工具.texture_filepath.relpath_convert_abspath(filepath, 相对贴图地址)
        插件材质.标签贴图绝对地址列表.append([标签, 绝对贴图地址])


def __贴图格式处理__(插件材质):
    match 数据.变量.贴图.贴图格式:
        case "dds": None
        case "png": __贴图格式转换__(插件材质)


def __贴图格式转换__(插件材质):
    indexlayer = int(数据.变量.贴图.Layer.split("_")[-1])
    indexmipmap = int(数据.变量.贴图.Mipmap.split("_")[-1])

    match 数据.变量.贴图.Data_Type:
        case "SRGB": datatype = 数据.变量.贴图.SRGB_Format
        case "UNORM": datatype = 数据.变量.贴图.UNORM_Format

    match 数据.变量.贴图.转换形式:
        case "重新生成贴图":
            for i, [标签, 绝对贴图地址] in enumerate(插件材质.标签贴图绝对地址列表):
                插件材质.标签贴图绝对地址列表[i][-1] = 工具.format_convert.dds_convert_to_png(绝对贴图地址, indexlayer, indexmipmap, datatype)
        case "引用现有贴图":
            for i, [标签, 绝对贴图地址] in enumerate(插件材质.标签贴图绝对地址列表):
                filepath_png = 绝对贴图地址[0:-4] + ".png"
                if os.path.exists(filepath_png):
                    插件材质.标签贴图绝对地址列表[i][-1] = filepath_png
                else:
                    插件材质.标签贴图绝对地址列表[i][-1] = 工具.format_convert.dds_convert_to_png(绝对贴图地址, indexlayer, indexmipmap, datatype)


