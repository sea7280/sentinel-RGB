import matplotlib.pyplot as plt
import tkinter as tk
from osgeo import gdal
import matplotlib.image as mpimg
import os
import sys
from PIL import ImageFile 
ImageFile.LOAD_TRUNCATED_IMAGES = True
sys.dont_write_bytecode = True
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

import parameter
import path


# RGB画像の生成
def truecolor(entry):
    filepath = path.pathGet(entry)
    setting_detail = parameter.getParameters(entry)

    bluepath  = filepath[0]
    greenpath = filepath[1]
    redpath   = filepath[2]

    # -------------------------------- カラー合成 -------------------------------
    band2_8bit_path = os.path.dirname(__file__) + "/Band2_8bit.tif"
    band3_8bit_path = os.path.dirname(__file__) + "/Band3_8bit.tif"
    band4_8bit_path = os.path.dirname(__file__) + "/Band4_8bit.tif"

    # 切り出しの詳細
    minX          = setting_detail[2]
    minY          = setting_detail[3]
    deltaX        = setting_detail[4]
    deltaY        = setting_detail[5]
    max_luminance = setting_detail[1]

    # 各バンドのファイルを、それぞれ、関心領域のみ切り出す。出力は8bitのgeotifとする
    # gdal.Translate({出力画像名}, {入力画像名}, outputType={データ形式設定} , scaleParams=[[min,max]], srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(
        band2_8bit_path,
        bluepath,
        scaleParams=[[0, max_luminance]],
        outputType=gdal.GDT_Byte,
        srcWin=[minX, minY, deltaX, deltaY],
    )
    gdal.Translate(
        band3_8bit_path,
        greenpath,
        scaleParams=[[0, max_luminance]],
        outputType=gdal.GDT_Byte,
        srcWin=[minX, minY, deltaX, deltaY],
    )
    gdal.Translate(
        band4_8bit_path,
        redpath,
        scaleParams=[[0, max_luminance]],
        outputType=gdal.GDT_Byte,
        srcWin=[minX, minY, deltaX, deltaY],
    )

    # 作成した8bitの切り出し画像を読み込む
    b2_image = gdal.Open(band2_8bit_path)
    b3_image = gdal.Open(band3_8bit_path)
    b4_image = gdal.Open(band4_8bit_path)

    # 読み込んだ画像を配列に変換する
    BlueBand_array = b2_image.ReadAsArray()
    GreenBand_array = b3_image.ReadAsArray()
    RedBand_array = b4_image.ReadAsArray()


    # 出力ファイルの設定のために、入力ファイルのX方向のピクセル数、Y方向のピクセル数を読み出す
    Xsize = b2_image.RasterXSize  # band2の画像のX方向ピクセル数
    Ysize = b2_image.RasterYSize  # band2の画像のY方向ピクセル数
    dtype = gdal.GDT_Byte
    band = 3

    # 出力ファイルの設定を行う(True Color)
    out_True_path = os.path.dirname(__file__) + "/truecolor.tif"  # 出力ファイル名

    # 空の出力ファイルを作成する
    out1 = gdal.GetDriverByName("GTiff").Create(
        out_True_path, Xsize, Ysize, band, dtype
    )  # ({出力ファイル名}, {X方向のピクセル数},{Y方向のピクセル数},{バンド数},{データ形式})

    # 出力ファイルの座標系を設定する
    out1.SetProjection(b2_image.GetProjection())  # {出力変数}.SetProjection(座標系情報)
    out1.SetGeoTransform(
        b2_image.GetGeoTransform()
    )  # {出力変数}.SetGeoTransform(座標に関する６つの数字)

    # Red、Green、Blueバンドの配列を、WriteArrayを用いて出力ファイルの3バンドに書き込む
    out1.GetRasterBand(1).WriteArray(RedBand_array)  # 赤の配列を赤バンドに書き込む
    out1.GetRasterBand(2).WriteArray(GreenBand_array)  # 緑の配列を緑バンドに書き込む
    out1.GetRasterBand(3).WriteArray(BlueBand_array)  # 青の配列を青バンドに書き込む
    out1.FlushCache()


    # ---------------------------------------- 出力 -----------------------------------------

    t = plt.figure(figsize=(7, 5))

    image1 = mpimg.imread(out_True_path)
    plt.imshow(image1)
    plt.title(setting_detail[6])
    #不要なので削除
    b2_image = None
    b3_image = None
    b4_image = None
    out1     = None
    os.remove(band2_8bit_path)
    os.remove(band3_8bit_path)
    os.remove(band4_8bit_path)
    os.remove(out_True_path)

    plt.show()
    plt.close()


