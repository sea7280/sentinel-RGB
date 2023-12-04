#ソフトウェアの起動ファイル

#ライブラリの読み込み
import tkinter as tk
import sys
sys.dont_write_bytecode = True

import ui as ui


#Applicationクラスの定義
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        #メインウィンドウの生成
        self.master.geometry("640x300")
        self.master.title("Sentinel-RGB")
        self.master.configure(bg="gray88")
        self.master.resizable(width=False, height=False)

        ui.ui(self.master)

#Applicationの実行関数
def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()
