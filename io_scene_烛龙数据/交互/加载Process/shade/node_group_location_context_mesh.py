from . import node_group_location_context

bl_idname_height_dict = node_group_location_context.bl_idname_height_dict


class 类(node_group_location_context.context):
    def __init__(self, x=0, y=0, padx=0, pady=0, rowsize=300, columnsize=300):
        node_group_location_context.context.__init__(self, x, y, padx, pady)
        self.rowsize = rowsize
        self.columnsize = columnsize
        # print(self.__class__, "提示：padx, pady, 设置将不起作用...")


    def __calc__location__(self, row, column):
        x = self.x
        for j in range(column): x -= self.columnsize
        y = self.y
        for i in range(row): y -= self.rowsize
        return x, y

