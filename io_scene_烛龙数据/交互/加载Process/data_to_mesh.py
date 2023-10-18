import bpy


def 新建网格(名称, 插件网格):
    mesh = bpy.data.meshes.new(名称)

    # 顶点
    顶点个数 = len(插件网格.顶点列表)
    mesh.vertices.add(顶点个数)
    positionxyzs = []
    for vx, vy, vz in 插件网格.顶点列表: positionxyzs += [vx, vy, vz]
    mesh.vertices.foreach_set("co", positionxyzs) # [x, y, z, x, y, z, ... ...]

    if 插件网格.顶点Loop列表 == []:
        mesh.validate()
        mesh.update()
        return mesh


    Loop个数 = len(插件网格.顶点Loop列表)
    步长 = 3
    面数 = len(插件网格.顶点Loop列表) // 步长

    # Loop
    mesh.loops.add(Loop个数)
    mesh.loops.foreach_set("vertex_index", 插件网格.顶点Loop列表) # [0, 1, 2, 1, 3, 4......]

    # 面
    mesh.polygons.add(面数)
    loop_start_list=[]
    loop_total_list=[]
    for i in range(0, Loop个数, 步长): # 若是四角面，则步长为4。# [[Loop索引左值, Loop个数], [Loop索引左值, Loop个数], ... ...]
        loop_start_list.append(i)
        loop_total_list.append(步长)
    mesh.polygons.foreach_set("loop_start", loop_start_list)
    mesh.polygons.foreach_set("loop_total", loop_total_list)

    # UV必须在面之后, 否则会出现长度预计为0的错误
    # loops_uv = [] # [u, v, u, v, u, v,... ...]
    # for i in 插件网格.顶点Loop列表:
    #     if 插件网格.顶点UV列表 == []: break
    #     loops_uv.append(插件网格.顶点UV列表[i][0])
    #     loops_uv.append(插件网格.顶点UV列表[i][1])
    # mesh.uv_layers.new()
    # mesh.uv_layers[0].data.foreach_set("uv", loops_uv)
    # mesh.validate()
    # mesh.update()

    mesh.uv_layers.new()
    for i, index in enumerate(插件网格.顶点Loop列表):
        if 插件网格.顶点UV列表 == []: break
        mesh.uv_layers[0].data[i].uv = 插件网格.顶点UV列表[index]
    mesh.validate()
    mesh.update()

    return mesh



