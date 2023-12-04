# パス取得

import glob
import sys

sys.dont_write_bytecode = True


def pathGet(entry):
    data_file = entry[0].get()
    filecheck = glob.glob(data_file + "/**/*10m", recursive=True)  # L2Aチェック
    l1c_check = glob.glob(data_file + "/**/*.jp2", recursive=True)  # Lc1チェック
    if len(filecheck) > 0:  # L2Aデータ
        R10m = filecheck[0]
        R20m = glob.glob(data_file + "/**/*20m", recursive=True)[0]
        bluepath = glob.glob(R10m + "/**B02_10m.jp2", recursive=True)[0]
        greenpath = glob.glob(R10m + "/**B03_10m.jp2", recursive=True)[0]
        redpath = glob.glob(R10m + "/**B04_10m.jp2", recursive=True)[0]
        nirpath = glob.glob(R10m + "/**B08_10m.jp2", recursive=True)[0]
        R_RE2path = glob.glob(R20m + "/**B06_20m.jp2", recursive=True)[0]
        R_SWIR1path = glob.glob(R20m + "/**B11_20m.jp2", recursive=True)[0]
    elif len(filecheck) == 0 and len(l1c_check) > 4:  # L1C
        bluepath = glob.glob(data_file + "/**/*B02.jp2", recursive=True)[0]
        greenpath = glob.glob(data_file + "/**/*B03.jp2", recursive=True)[0]
        redpath = glob.glob(data_file + "/**/*B04.jp2", recursive=True)[0]
        nirpath = glob.glob(data_file + "/**/*B08.jp2", recursive=True)[0]
        R_RE2path = glob.glob(data_file + "/**/*B06.jp2", recursive=True)[0]
        R_SWIR1path = glob.glob(data_file + "/**/*B11.jp2", recursive=True)[0]
    else:
        bluepath = None  # 初期設定
        greenpath = None  # 初期設定
        redpath = None  # 初期設定
        nirpath = None  # 初期設定
        R_RE2path = None  # 初期設定
        R_SWIR1path = None  # 初期設定
        type_sentinel = 1

    satellite_data_list = [
        bluepath,  # 0
        greenpath,  # 1
        redpath,  # 2
        nirpath,  # 3    
        ]

    return satellite_data_list
