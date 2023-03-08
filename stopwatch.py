import datetime
import PySimpleGUI as sg
sg.theme("DarkBrown3")

# ストップウォッチアプリのレイアウト
# フォントはArial、サイズは40、位置は中央
layout = [[sg.T("0:00:00.000000", font=("Arial",40), k="txt",
           size=(15,1), justification="center")],
          [sg.Push(), sg.B("START/STOP", k="btn"),sg.Push()]]
win = sg.Window("ストップウォッチ", layout, 
                font=(None,14), size=(400,120), keep_on_top=True)

# ストップウォッチの実行
def execute():
    if startflag == True:
        now = datetime.datetime.now()
        td = now - start
        win["txt"].update(td)

def startstop():
    global start, startflag
    if startflag == True:
        startflag = False
    else:
        start =datetime.datetime.now()
        startflag = True

startflag = False
while True:
    e, v = win.read(timeout=50)
    execute()
    if e == "btn":
        startstop()
    if e == None:
        break
win.close()