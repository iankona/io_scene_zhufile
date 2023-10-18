from . import node_group_location_context


bl_idname_height_dict = node_group_location_context.bl_idname_height_dict


class 类(node_group_location_context.context):
    def __init__(self, x=0, y=0, padx=50, pady=50):
        node_group_location_context.context.__init__(self, x, y, padx, pady)



    def __calc__location__(self, row, column):
        x = self.x
        for j in range(column+1): 
            x -= self.columnmaxwidth[j]
            if self.columnmaxwidth[j] == 0: continue
            x -= self.padx

        y = self.y
        for i in range(row): 
            node = self.groups[column][i]
            if node == None: continue
            if node.bl_idname in bl_idname_height_dict:
                height = bl_idname_height_dict[node.bl_idname]
            else:
                height = 200
            y -= height
            y -= self.pady
        return x, y
    




