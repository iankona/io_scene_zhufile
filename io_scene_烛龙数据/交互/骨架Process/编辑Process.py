import os

import bpy

from ... import 数据, 接口



def 骨骼长度处理():
    match 数据.变量.骨架.骨骼长度处理模式:
        case '自动处理': [__计算__骨骼长度__(插件数据.插件骨架) for 插件数据 in 数据.变量.选择集.插件数据列表]
        case '原始数据': [__原始__骨骼长度__(插件数据.插件骨架) for 插件数据 in 数据.变量.选择集.插件数据列表]
        case '手动设置': [__设置__骨骼长度__(插件数据.插件骨架) for 插件数据 in 数据.变量.选择集.插件数据列表]


def __计算__骨骼长度__(插件骨架):
    if 插件骨架 == None: return ""

    for 骨骼名称, 插件骨骼 in 插件骨架.骨骼字典.items():
        if 插件骨骼.parent is None: continue
        插件骨骼.parent.children.append(插件骨骼)

    for 骨骼名称, 插件骨骼 in 插件骨架.骨骼字典.items():
        if 插件骨骼.children == []:
            if 插件骨骼.parent is None: 插件骨骼.length = (插件骨骼.tail - 插件骨骼.head).length
            else: 插件骨骼.length = 插件骨骼.parent.length
        else:
            count, length = 0, 0.0
            for child in 插件骨骼.children:
                count += 1
                length += (插件骨骼.head - child.head).length
            插件骨骼.length = length / count

    for 骨骼名称, 插件骨骼 in 插件骨架.骨骼字典.items():
        if 插件骨骼.length  < 0.001: 插件骨骼.length = 0.001


def __原始__骨骼长度__(插件骨架):
    if 插件骨架 == None: return ""
    for 骨骼名称, 插件骨骼 in 插件骨架.骨骼字典.items():
        插件骨骼.length = (插件骨骼.tail - 插件骨骼.head).length


def __设置__骨骼长度__(插件骨架):
    if 插件骨架 == None: return ""
    length = float(数据.变量.骨架.骨骼长度)
    for 骨骼名称, 插件骨骼 in 插件骨架.骨骼字典.items():
        插件骨骼.length = length






