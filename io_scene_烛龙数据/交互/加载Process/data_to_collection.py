

import bpy
import traceback
from ... import 数据



def 新建选择集(名称):
    collection = bpy.data.collections.new(名称)
    bpy.context.scene.collection.children.link(collection)
    return collection










