#各パラメータ取得


def getParameters(entry):

#entryの入力値を配列に格納
    filePath       = entry[0].get()
    luminance      = int(entry[1].get())
    minX           = int(entry[2].get())
    minY           = int(entry[3].get())
    deltaX         = int(entry[4].get())
    deltaY         = int(entry[5].get())
    title          = entry[6].get()

#変数：setting_detail
    setting_detail = [filePath,         #0
                      luminance,        #1
                      minX,             #2
                      minY,             #3
                      deltaX,           #4
                      deltaY,           #5
                      title,            #6
                      ] 
    
    return setting_detail
