import PySimpleGUI as sg
import datetime
sg.theme("DarkBrown3")

# 現在時刻を表示するアプリ
# フォントはArial、サイズは40、位置は中央
# ウインドウサイズは400x80、常に最前面に表示
layout = [[sg.T("0000/00/00 (---)", font=("Arial",40), k="txt2",
                size=(20,1), justification="center")],
            [sg.T("AM 00:00:00", font=("Arial",40), k="txt1",
                size=(20,1), justification="center")]]
win = sg.Window("時計", layout, size=(480,150), keep_on_top=True)

def execute():
    now = datetime.datetime.now()
    win["txt2"].update(f"{now:%Y/%m/%d (%a)}")
    win["txt1"].update(f"{now:%p %H:%M:%S}")

while True:
    e, v = win.read(timeout=500)
    execute()
    if e == None:
        break
win.close()