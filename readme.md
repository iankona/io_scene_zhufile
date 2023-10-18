<div align="center" style="font-size: 42px; font-weight:bold;">io_scene_烛龙数据</div>
---

```py
# Nothing happened here in this code, don't mind about it
from . import 工具, 交互, 接口, 界面, 数据, 文件
```



## 一、插件 io_scene_烛龙数据\_2.6.4\_Blender3.6.4，存档版本。

Blender逐渐发展，再次遇到了兼容性问题。笔者以前了解到的第1次兼容问题，是Blender2.49b升级Blender5.0时.blend存储文件不能直接互相读取；第2次则是现在，Blender3.6.4升级Blender4.0时，只有Blender3.6.4这个版本能正常读取Blender4.0的.blend文件，其他的Blender2.8，Blender3.0等旧版本，想打开Blender4.0的.blend文件，只能通过Blender3.6.4中转，读取新的.blend文件，再保存1次，.blend文件才会变成旧版本。而Blender4.0则是能正常读取旧.blend文件。

除开.blend工程文件的兼容性问题，笔者印象中，Blender的api大概也有2次的改动比较大，让笔者印象深刻，一是Blender2.8的发布，让笔者觉得api比较稳定插件可以开始着手编制，二是Blender3.4的发布，笔者想直接查看Blender界面代码只能用Blender3.3。

随着2023年10月份，Blender4.0Beta的发布，从blender4.0Beta这次的.blender工程文件改动兼容情况和blender python api的改动情况来看，大概率本插件的材质部分代码将失效。而插件的维护，以后也将移到Blender4.0上，故近期整理代码，形成插件 io_scene_烛龙数据\_2.6.4\_Blender3.6.4，作为1个存档版本留存。简记于2023年10月17日。



## 二、插件简介

本插件主要用于导入上海烛龙信息科技有限公司（Aurogon Info&Tech (Shanghai) Co., Ltd.）开发发行的《[古剑奇谭：琴心剑魄今何在]("")》（2010年07月10日）、《[古剑奇谭二：永夜初晗凝碧天]("")》（2013年8月18日）、《[古剑奇谭三：梦付千秋星垂野]("")》（2018年11月23日）三款游戏的解包数据文件到Blender3.6.4软件中，注：本存档版本不支持Blender4.0。

本插件也支持旧引擎版本的《[古剑奇谭网络版（Swords of Legends Online）]("")》游戏解包文件导入到Blender软件中。古剑奇谭网络版与古剑3使用相同的游戏引擎，相同的model文件5版本，故本插件能正常把旧古网文件导入到Blender3.3-3.6。后续古网若升级了文件版本、或者升级了游戏引擎版本，或者更换了游戏引擎，则本插件不能保证正常导入，您依然可以用本插件尝试导入新版本的解包游戏文件。

本插件仅支持古剑1古剑2古剑3三代游戏解包文件，后续的古剑奇谭系列新单机游戏，本插件不支持其解包文件导入。2020年7月11日烛龙官方在嘉年华现场发布消息，古剑奇谭网络版和古剑奇谭系列后续单机游戏，将更换成虚幻4游戏引擎。

本插件能处理的文件夹目录结构为RPGViewer解包出来的文件及文件夹，请使用RPGViewer30Build20210920软件的顶部菜单功能，【打开游戏目录】和【左侧全选-addon-压缩包操作-批量解包-设置输出目录-解包游戏】，完整解包游戏。

本插件要求Blender软件版本需达到3.3及以上。由于本插件大量使用python的match case语法，因此Blender内置的python版本需要在3.10及以上。



## 三、支持的文件格式

**古剑1**


- **nif**:　gamebryo游戏引擎，引擎版本V20.6.0.0，模型及场景文件。

- **kf**: 　gamebryo游戏引擎，引擎版本V20.6.0.0，动画文件。

**古剑2**


- **xac**:　Vision Engine游戏引擎，引擎版本V8.0，Emotion Fx模型文件。

- **xsm**: 　Vision Engine游戏引擎，引擎版本V8.0，Emotion Fx动画文件。

- **vmesh**:  　Vision Engine游戏引擎，引擎版本V8.0，havok静态场景部件模型，文件版本V1。

- **model**:  　Vision Engine游戏引擎，引擎版本V8.0，havok模型，文件版本V1。

- **srt**:  　Vision Engine游戏引擎，引擎版本V8.0，speedtree模型，文件版本SRT 05.2.0。

**古剑3**


- **model**:　Vision Engine游戏引擎，引擎版本未知，havok模型文件，文件版本V5。

- **morph**: 　Vision Engine游戏引擎，引擎版本未知，havok表情文件，文件版本V5。。

- **avatar**: 　Vision Engine游戏引擎，引擎版本未知，havok角色文件。

- **hka**: 　Vision Engine游戏引擎，引擎版本未知，havok动画文件，文件版本hk_2014.2.0-r1。

- **srt**:  　Vision Engine游戏引擎，引擎版本未知，speedtree模型，文件版本SRT 07.0.0。



## 四、说明

[插件历程]("插件历程.md")

[功能说明]("功能说明.docx")

[安装教程]("安装教程.docx")



## 五、参考

十分感谢为本插件的编制提供帮助的人们。

最后，感谢插件所参考的软件项目的公开代码，这些代码使得Blender古剑游戏系列导入插件，在今天得以以1个较稳定的版本发布。由于插件开发时间跨度接近5年，作者不能一一记起和列举插件所参考的全部开源项目，这里十分感谢这些作者在文件解析方面和导入Blender方面所做的探索，这些探索为插件开发提供了一个良好的基础。

古剑一nif、kf部分主要参考[Noesis](http://www.richwhitehouse.com/index.php?content=inc_projects.php)软件和[ponyrider0](https://github.com/ponyrider0)’s  FarNifAutoGen项目
- written in part using RichwhiteHouse's Noesis's fmt_gamebryo_nif.py as a reference 
- Noesis is a tool for previewing and converting between hundreds of model, image, and animation formats. 
- https://github.com/ponyrider0/FarNifAutoGen/blob/master/import_nif_con.py  if rotation_type == 4:

古剑二xac, xsm部分主要参考了**[Szkaradek123](https://forum.xentax.com/memberlist.php?mode=viewprofile&u=26056)** 的插件Blender249\[Gujian2\]\[xac\]\[xsm\]\[2015-03-02\].zip和[enenra](https://github.com/enenra)’s [x4modding](https://github.com/enenra/x4modding)开源项目的xac, xsm文件格式资料

- https://github.com/enenra/x4modding/wiki/Model-file-infomation-(_arc)
- https://forum.xentax.com/viewtopic.php?t=12641

古剑三hka动画部分主要参考了[Meowmaritus](https://github.com/Meowmaritus)‘s MVDX2开源项目和[OpenAWE-Project](https://github.com/OpenAWE-Project)‘s OpenAWE开源项目
- https://github.com/Meowmaritus/MVDX2/blob/master/MVDX2/Havok/SplineCompressedAnimation.cs
- https://github.com/OpenAWE-Project/OpenAWE/blob/master/src/awe/havokfile.cpp
- https://github.com/zephenryus/havok-reflection

古剑二/古剑三的SpeedTree Real-Time Model (.srt)文件主要参考了[WolvenKit-7](https://github.com/WolvenKit/WolvenKit-7)软件和[io_scene_srt_json](https://github.com/ArdCarraigh/Blender_SRT_JSON_Addon)Blender插件
-  https://github.com/WolvenKit/WolvenKit/blob/main/WolvenKit.Common/RED3/SRT/Srtfile.cs

