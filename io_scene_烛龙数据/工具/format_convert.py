
import os
import subprocess

def dds_convert_to_png(filepath="", indexlayer=0, indexmipmap=0, datatype="RGBA8_UNORM"): # 每次调用，都是强制覆盖
    exepath = f"\"{os.path.dirname(os.path.realpath(__file__))}\\ImageViewer3_7_lite\\ImageConsole.exe\" "
    open = f"-open "
    filepathi = filepath + " "
    layer = f"-exportlayer {indexlayer} "
    mipmap = f"-exportmipmap {indexmipmap} "
    quality = f"-exportquality 100 "
    export =  f"-export "
    filepatho = filepath[0:-4] + ".png "
    # datatype = f"RGBA8_UNORM"
    command = exepath + open + filepathi + layer + mipmap + quality + export + filepatho + datatype
    subprocess.call(command)
    return filepatho


def 测试(filepathi="", indexlayer=0, indexmipmap=0, filepatho="", datatype="RGBA8_UNORM"):
    exepath = f"\"{os.path.dirname(os.path.realpath(__file__))}\\ImageViewer3_7_lite\\ImageConsole.exe\" "
    open = f"-open "
    filepathi = f"C:\\Users\\wdy\\Desktop\\ces\\actress1_default_body_01d.dds "
    layer = f"-exportlayer {indexlayer} "
    mipmap = f"-exportmipmap {indexmipmap} "
    quality = f"-exportquality 100 "
    export =  f"-export "
    filepatho = f"C:\\Users\\wdy\\Desktop\\ces\\actress1_default_body_01d.png "
    datatype = f"RGBA8_UNORM"
    command = exepath + open + filepathi + layer + mipmap + quality + export + filepatho + datatype
    subprocess.call(command)

# ImageConsole.exe -help
# Commands:
# -addfilter "file1" ["file2" ...]                      adds all filter to the pipeline
# -cin                                                  keeps the console open to retrieve commands via cin
# -close                                                stops reading from cin
# -delete [index]                                       deletes the image with the specified index or all images if no index was specified
# -deletefilter [index]                                 deletes the filter with the given index or all filter if no index is given
# -deletemipmaps                                        keeps only the most detailed mipmap
# -equation "color equation" ["alpha equation"]         sets image combine equations
# -export filename gliFormat                            saves the current image with the filename
# -exportcrop true/false [xStart yStart xEnd yEnd]      enables/disables export cropping and sets cropping boundaries
# -exportlayer layer                                    sets the layer that should be exported. -1 means all layers
# -exportmipmap mipmap                                  sets the mipmap that should be exported. -1 means all mipmaps
# -exportquality quality                                sets the quality level for jpg exports. Between 1 and 100
# -filterparam index "param name" value                 sets the parameter of the filter at index
# -genmipmaps                                           (re)generates mipmaps
# -help                                                 lists all commands
# -move oldIndex newIndex                               moves the image to the given image index
# -open "file1" "file2" ...                             imports all filenames as images
# -silent                                               disables progress output
# -ssim imageId1 imageId2                               prints ssim of the two input images
# -stats "min/max/avg" "luminance/luma/avg/lightness"   prints the statistic
# -tellalpha                                            prints true if any pixel has alpha that is not 1
# -tellfilter                                           prints list of filters
# -tellfilterparams index                               prints the filter parameters of the filter at index
# -tellformats "file extension"                         prints the available export formats for a specific file extension
# -telllayers                                           print number of layers
# -tellmipmaps                                          prints number of mipmaps
# -tellpixel x y [layer mipmap radius]                  prints the pixel color in linear and in srgb
# -tellsize [mipmapIndex]                               prints the width and height of the mipmap
# -thumbnail size                                       creates a thumbnail with the specified size and returns byte stream




