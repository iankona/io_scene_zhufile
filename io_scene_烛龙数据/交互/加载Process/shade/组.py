




def node_group_sqrt_1r5g5(材质, material, 贴图路径, check_existing, node_principled_bsdf):
    # sqrt(1-(2*(R-0.5))²+(2*(G-0.5))²)
    node_texture_image = material.node_tree.nodes.new(type='ShaderNodeTexImage')
    node_texture_image.location = [-1800, -100]
    node_texture_image.image = bpy.data.images.load(贴图路径, check_existing=check_existing)
    node_texture_image.image.colorspace_settings.name = 'Non-Color'
    node_separate_rgb = material.node_tree.nodes.new(type='ShaderNodeSeparateRGB') # 分离rgb
    node_separate_rgb.location = [-1600, -100]

    material.node_tree.links.new(node_texture_image.outputs["Color"], node_separate_rgb.inputs["Image"])
    node_combine_rgb = material.node_tree.nodes.new(type='ShaderNodeCombineRGB') # 合并rgb
    node_combine_rgb.location = [-400, -82]

    material.node_tree.links.new(node_separate_rgb.outputs["R"], node_combine_rgb.inputs["R"])
    material.node_tree.links.new(node_separate_rgb.outputs["G"], node_combine_rgb.inputs["G"])

    # R-0.5相减
    node_r_subtrtact_05 = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_r_subtrtact_05.operation = 'SUBTRACT'
    node_r_subtrtact_05.location = [-1400, -200]
    node_r_subtrtact_05.inputs[1].default_value = 0.5
    material.node_tree.links.new(node_separate_rgb.outputs["R"], node_r_subtrtact_05.inputs[0])

    # G-0.5相减
    node_g_subtrtact_05 = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_g_subtrtact_05.operation = 'SUBTRACT'
    node_g_subtrtact_05.location = [-1400, -400]
    node_g_subtrtact_05.inputs[1].default_value = 0.5
    material.node_tree.links.new(node_separate_rgb.outputs["G"], node_g_subtrtact_05.inputs[0])

    # R-0.5乘以2
    node_2_subtrtact_r05 = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_2_subtrtact_r05.operation = 'MULTIPLY'
    node_2_subtrtact_r05.location = [-1200, -200]
    node_2_subtrtact_r05.inputs[0].default_value = 2
    material.node_tree.links.new(node_r_subtrtact_05.outputs[0], node_2_subtrtact_r05.inputs[1])

    # G-0.5乘以2
    node_2_subtrtact_g05 = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_2_subtrtact_g05.operation = 'MULTIPLY'
    node_2_subtrtact_g05.location = [-1200, -400]
    node_2_subtrtact_g05.inputs[0].default_value = 2
    material.node_tree.links.new(node_g_subtrtact_05.outputs[0], node_2_subtrtact_g05.inputs[1])

    # R平方
    node_r_multiply = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_r_multiply.operation = 'MULTIPLY'
    node_r_multiply.location = [-1000, -200]
    material.node_tree.links.new(node_2_subtrtact_r05.outputs[0], node_r_multiply.inputs[0])
    material.node_tree.links.new(node_2_subtrtact_r05.outputs[0], node_r_multiply.inputs[1])

    # G平方
    node_g_multiply = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_g_multiply.operation = 'MULTIPLY'
    node_g_multiply.location = [-1000, -400]
    material.node_tree.links.new(node_2_subtrtact_g05.outputs[0], node_g_multiply.inputs[0])
    material.node_tree.links.new(node_2_subtrtact_g05.outputs[0], node_g_multiply.inputs[1])

    # 相加
    node_r2_add_g2 = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_r2_add_g2.operation = 'ADD'
    node_r2_add_g2.location = [-800, -300]


    material.node_tree.links.new(node_r_multiply.outputs[0], node_r2_add_g2.inputs[0])
    material.node_tree.links.new(node_g_multiply.outputs[0], node_r2_add_g2.inputs[1])
    # 1相减
    node_1_subtrtact_r2g2 = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_1_subtrtact_r2g2.operation = 'SUBTRACT'
    node_1_subtrtact_r2g2.location = [-600, -300]
    node_1_subtrtact_r2g2.inputs[0].default_value = 1
    material.node_tree.links.new(node_r2_add_g2.outputs[0], node_1_subtrtact_r2g2.inputs[1])
    # 开平方根
    node_sqrt_1_r2g2 = material.node_tree.nodes.new(type='ShaderNodeMath') # 运算
    node_sqrt_1_r2g2.operation = 'SQRT'
    node_sqrt_1_r2g2.location = [-400, -300]

    material.node_tree.links.new(node_1_subtrtact_r2g2.outputs[0], node_sqrt_1_r2g2.inputs[0])
    material.node_tree.links.new(node_sqrt_1_r2g2.outputs[0], node_combine_rgb.inputs["B"])

    # material.node_tree.links.new(node_combine_rgb.outputs["Image"], node_principled_bsdf.inputs["Normal"])
    node_normalmap = material.node_tree.nodes.new(type='ShaderNodeNormalMap')
    node_normalmap.location = [-200, -100]
    if 材质.古剑标签 == "古剑3":
        if 数据.变量.古剑3_法线贴图空间 == "切线空间": node_normalmap.space = 'TANGENT'
        if 数据.变量.古剑3_法线贴图空间 == "物体空间": node_normalmap.space = 'OBJECT'
        if 数据.变量.古剑3_法线贴图空间 == "世界空间": node_normalmap.space = 'WORLD'
        if 数据.变量.古剑3_法线贴图空间 == "Blender物体空间": node_normalmap.space = 'BLENDER_OBJECT'
        if 数据.变量.古剑3_法线贴图空间 == "Blender世界空间": node_normalmap.space = 'BLENDER_WORLD'

    if 材质.古剑标签 == "古剑1" or 材质.古剑标签 == "古剑2": node_normalmap.space = 'BLENDER_OBJECT'
    material.node_tree.links.new(node_combine_rgb.outputs["Image"], node_normalmap.inputs["Color"])
    material.node_tree.links.new(node_normalmap.outputs["Normal"], node_principled_bsdf.inputs["Normal"])