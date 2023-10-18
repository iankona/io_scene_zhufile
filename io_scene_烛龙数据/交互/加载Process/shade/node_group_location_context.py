

bl_idname_height_dict = {
    'ShaderNodeOutputMaterial': 115,
    'ShaderNodeBsdfPrincipled': 620,
    'ShaderNodeTexImage': 265,
    'ShaderNodeSeparateRGB':115,
    'ShaderNodeCombineRGB': 115,
    'ShaderNodeMath':146,
    'ShaderNodeNormalMap':145,
    'ShaderNodeGamma':94,
    'ShaderNodeInvert':94,
}




class context:
    def __init__(self, x, y, padx, pady):
        self.x = x
        self.y = y
        self.groups = []
        self.padx = padx
        self.pady = pady
        self.rowmaxindex = 0
        self.columnmaxindex = 0
        self.rowmaxheight = []
        self.columnmaxwidth = []
        self.__init__group__setting__()


    def __init__group__setting__(self):
        for j in range(11): # 新建列
            nodes = [None for i in range(11)] # 新建行
            self.groups.append(nodes)
        self.rowmaxindex += 10
        self.columnmaxindex += 10
        self.rowmaxheight = [0 for i in range(11)]
        self.columnmaxwidth = [0 for j in range(11)]


    def add_node(self, node, row=0, column=0):
        if row < 0 or column < 0: raise ValueError("输入的行列索引为负值，应为正值！")
        self.__add__node__(row, column)
        self.groups[column][row] = node
        self.__update__node__location__(row, column)


    def __add__node__(self, row, column):
        if row > self.rowmaxindex: # 更新行
            for nodes in self.groups:
                for i in range(row-self.rowmaxindex+1): nodes.append(None)
            self.rowmaxindex = row
            for i in range(row-self.rowmaxindex+1): self.rowmaxheight.append(0)

        if column > self.columnmaxindex: # 更新列
            for j in range(column-self.columnmaxindex+1):
                nodes = [None for i in range(self.rowmaxindex+1)]
                self.groups.append(nodes)
            self.columnmaxindex = column
            for j in range(column-self.columnmaxindex+1): self.columnmaxwidth.append(0)


    def __update__maxwidth__maxheight__(self, row, column):
        for i in range(row+1): 
            node = self.groups[column][i]
            if node == None: continue
            if node.width > self.columnmaxwidth[column]: self.columnmaxwidth[column] = node.width

        for j in range(column+1):
            node = self.groups[j][row]
            if node == None: continue
            if node.bl_idname in bl_idname_height_dict:
                height = bl_idname_height_dict[node.bl_idname]
            else:
                height = 200
            if height > self.rowmaxheight[row]: self.rowmaxheight[row] = height


    def __calc__location__(self, row, column):
        pass


    def __update__node__location__(self, row, column):
        self.__update__maxwidth__maxheight__(row, column)
        for j in range(self.columnmaxindex+1):
            for i in range(self.rowmaxindex+1):
                node = self.groups[j][i]
                if node == None: continue
                node.location = self.__calc__location__(i, j)

    
    def __calc__bbox__(self, row, column):
        x = self.x
        for j in range(column+1): 
            x -= self.columnmaxwidth[j]
            if self.columnmaxwidth[j] == 0: continue
            x -= self.padx

        y = self.y
        for i in range(row+1): 
            y -= self.rowmaxheight[i]
            if self.rowmaxheight[i] == 0: continue
            y -= self.pady
        return x, y


    # 上北下南，左西右东
    #   n   s     w   e
    def context_wn(self):
        self.__update__maxwidth__maxheight__(self.rowmaxindex, self.columnmaxindex)
        x, y = self.__calc__bbox__(self.rowmaxindex, self.columnmaxindex)
        context = self.__class__(x, self.y, self.padx, self.pady)
        return context

    def context_ws(self):
        self.__update__maxwidth__maxheight__(self.rowmaxindex, self.columnmaxindex)
        x, y = self.__calc__bbox__(self.rowmaxindex, self.columnmaxindex)
        context = self.__class__(x, y, self.padx, self.pady)
        return context

    def context_es(self):
        self.__update__maxwidth__maxheight__(self.rowmaxindex, self.columnmaxindex)
        x, y = self.__calc__bbox__(self.rowmaxindex, self.columnmaxindex)
        context = self.__class__(self.x, y, self.padx, self.pady)
        return context
    
    
    def context_w(self):
        self.__update__maxwidth__maxheight__(self.rowmaxindex, self.columnmaxindex)
        x, y = self.__calc__bbox__(self.rowmaxindex, self.columnmaxindex)
        context = self.__class__(x, self.y//2, self.padx, self.pady)
        return context

    def context_s(self):
        self.__update__maxwidth__maxheight__(self.rowmaxindex, self.columnmaxindex)
        x, y = self.__calc__bbox__(self.rowmaxindex, self.columnmaxindex)
        context = self.__class__(self.x//2, y, self.padx, self.pady)
        return context