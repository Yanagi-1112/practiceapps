import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.T("指定された年の干支を調べます。")],
          [sg.T("西暦何年ですか？"), sg.I("2022", k="in1")],
          [sg.B("実行", k="btn")],
          [sg.T(k="txt")]]
win = sg.Window("干支アプリ", layout,
                font=(None,14), size=(320,150))

def execute():
    eto = ["子（ねずみ）", "丑（うし）", "寅（とら）", "卯（うさぎ）", "辰（たつ）", "巳（み）", "午（うま）", "未（ひつじ）", "申（さる）", "酉（とり）", "戌（いぬ）", "亥（いのしし）"]
    in1 = int(v["in1"])
    etonum = (in1 - 4) % 12
    txt = f"{in1}年は、{eto[etonum]}年です。"
    win["txt"].update(txt)

while True:
    e, v = win.read()
    if e == "btn":
        execute()
    if e is None:
        break
win.close()