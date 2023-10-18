
# ('F:\\io_scene_烛龙数据\\交互\\加载Lanuch', '.py')
# ('F:\\io_scene_烛龙数据\\交互\\加载Lanuch', '')
# ('', '')
# ('../desk/.obh', '')
# ('../desk/ad_d', '.obh')
from ... import 数据, 文件

import os

from . import struct_from_fbx
from . import struct_from_nif
from . import struct_from_kf
from . import struct_from_xac
from . import struct_from_xsm
from . import struct_from_vmesh
from . import struct_from_model
from . import struct_from_hka
from . import struct_from_hkx
from . import struct_from_avatar
from . import struct_from_srt



def 函数():
    for filepath in 数据.变量.选择集.filepaths:
        filedata = __filepath__to__filedata__(filepath)
        数据.变量.选择集.filedatas.append(filedata)

    for filedata in 数据.变量.选择集.filedatas:
        filestruct = __filedata__to__filestruct__(filedata)
        filestruct.struct_to_插件数据(数据.变量.选择集)


def __filepath__to__filedata__(filepath):
    bp = 文件.bpformat.bpnumpy.类().filepath(filepath)
    match os.path.splitext(filepath)[-1]:
        case ".fbx":    filedata = 文件.fbx.类(bp)
        case ".nif":    filedata = 文件.nif.类(bp)
        case ".kf":     filedata = 文件.kf.类(bp)
        case ".xac":    filedata = 文件.xac.类(bp)
        case ".xsm":    filedata = 文件.xsm.类(bp)
        case ".vmesh":  filedata = 文件.vmesh.类(bp)
        case ".model":  filedata = 文件.model.类(bp)
        case ".hka":    filedata = 文件.hka.类(bp)
        case ".hkx":    filedata = 文件.hkx.类(bp)
        case ".avatar": filedata = 文件.avatar.类(bp)
        case ".srt":    filedata = 文件.srt.类(bp)
        case _:  raise  ValueError(f"未支持的文件格式：{filepath}")
    bp.close()
    return filedata        


def __filedata__to__filestruct__(filedata):
    match os.path.splitext(filedata.filepath)[-1]:
        case ".fbx":    filestruct = struct_from_fbx.类(filedata)
        case ".nif":    filestruct = struct_from_nif.类(filedata)
        case ".kf":     filestruct = struct_from_kf.类(filedata)
        case ".xac":    filestruct = struct_from_xac.类(filedata)
        case ".xsm":    filestruct = struct_from_xsm.类(filedata)
        case ".vmesh":  filestruct = struct_from_vmesh.类(filedata)
        case ".model":  filestruct = struct_from_model.类(filedata)
        case ".hka":    filestruct = struct_from_hka.类(filedata)
        case ".hkx":    filestruct = struct_from_hkx.类(filedata)
        case ".avatar": filestruct = struct_from_avatar.类(filedata)
        case ".srt":    filestruct = struct_from_srt.类(filedata)
    return filestruct

