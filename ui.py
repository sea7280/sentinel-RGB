#UI画面

import tkinter as tk
import sys
sys.dont_write_bytecode = True
from tkinter.scrolledtext import ScrolledText

import rgb
import load
import write_excel

#フレームの生成関数
def create_frame(master):
    mainFrame = tk.Frame(master, height=300, width=700, bg="gray88")
    mainFrame.place(x=0, y=0)

    return mainFrame

#ラベル生成
def create_label(area):
    setteingFrame = area
    background = "gray88"
    fontcolor = "black"

########################################################################################################
################################################# main #################################################
    setpositionY = 10

    label = tk.Label(setteingFrame, text=u'Sentinel RGB Image creater'
                                                            , bg=background, fg=fontcolor, font=("",18)).place(x=25, y=setpositionY - 5)
    label = tk.Label(setteingFrame, text=u'Data:'           , bg=background, fg=fontcolor, font=("",15)).place(x=25, y=setpositionY + 30)
    label = tk.Label(setteingFrame, text=u'Luminance'       , bg=background, fg=fontcolor, font=("",15)).place(x=90, y=setpositionY + 70)
    label = tk.Label(setteingFrame, text=u'Top left point'  , bg=background, fg=fontcolor, font=("",15)).place(x=90, y=setpositionY + 100)
    label = tk.Label(setteingFrame, text=u':'               , bg=background, fg=fontcolor, font=("",15)).place(x=303,y=setpositionY + 101)
    label = tk.Label(setteingFrame, text=u'Sampling range'  , bg=background, fg=fontcolor, font=("",15)).place(x=90, y=setpositionY + 130)
    label = tk.Label(setteingFrame, text=u'×'               , bg=background, fg=fontcolor, font=("",15)).place(x=297,y=setpositionY + 131)
    label = tk.Label(setteingFrame, text=u'title'           , bg=background, fg=fontcolor, font=("",15)).place(x=90, y=setpositionY + 160)

#entry作成関数
def create_entry(area):
    #出力先を指定
    settingsArea = area
    #背景色、フォントカラーの指定
    background = "white"
    fontcolor = "black"
    
    #出力座標の基準位置
    setpositionY = 10

    #entryの生成
    entry_file         = tk.Entry(settingsArea, width=50, bg=background, fg=fontcolor, font=("", 14))
    entry_lumi         = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_px           = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_py           = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_deltaX       = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_deltaY       = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_plt_title    = tk.Entry(settingsArea, width=25, bg=background, fg=fontcolor, font=("", 14))

    #entry設置

    entry_file.place(        x=80,y=setpositionY  + 35)
    entry_lumi.place(        x=260,y=setpositionY + 72)
    entry_px.place(          x=220,y=setpositionY + 102)
    entry_py.place(          x=320,y=setpositionY + 102)
    entry_deltaX.place(      x=220,y=setpositionY + 132)
    entry_deltaY.place(      x=320,y=setpositionY + 132)
    entry_plt_title.place(   x=260,y=setpositionY + 162)
    
    #enrtyに初期値を設定
    entry_lumi.insert(0,10000)
    entry_px.insert(0,0)
    entry_py.insert(0,0)
    entry_deltaX.insert(0,0)
    entry_deltaY.insert(0,0)
    entry_plt_title.insert(0,"data")

    #生成したentryを配列で保持
    entry_list = [entry_file        #0
                ,entry_lumi         #1
                ,entry_px           #2
                ,entry_py           #3
                ,entry_deltaX       #4
                ,entry_deltaY       #5
                ,entry_plt_title    #6
                ]
    #entry_listを返す
    return entry_list

############################################################################################################
################################################# ボタン生成 #################################################
def create_button(area, entry_list):
    
        background = "gray88"
        fontcolor = "black"
#衛星データファイルの読み込みボタン
        Button = tk.Button(area,text=u'...', bg=background, fg=fontcolor, command=lambda:load.load_dataFile(entry_list[0])
                          )
        Button.place(x=550, y=43, height=30 , width=30)
#RGB画像生成
        Button = tk.Button(area,text=u'RGB', bg=background, fg=fontcolor, command=lambda:rgb.truecolor(entry_list))
        Button.place(x=180, y=220, height=50 , width=110)
#エクセルに保存
        #def write_excel():
        #        excel.saveExcel(parameters)
        Button = tk.Button(area,text=u'Save Excel', bg=background, fg=fontcolor, command=lambda:write_excel.saveExcel(entry_list))
        Button.place(x=330, y=220, height=50 , width=110)


############################################################################################################
################################################### 実行 ###################################################

def ui(master):
    frame = create_frame(master)
    create_label(frame)
    entry = create_entry(frame)
    create_button(frame, entry)