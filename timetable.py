import PySimpleGUI as sg
import datetime
sg.theme("DarkBrown3")

# 現在時刻と、6時限までの時間割を表示するアプリ
# フォントはArial、サイズは40、位置は中央
# ウインドウサイズは450x260、常に最前面に表示
# タイトルは「時間割アプリ」
# 時間割は、1限目から6限目まであり、現在時刻からの残り時間を表示する
# 1時限目は8:50から、2時限目は10:30から、昼休みは12:40から、3時限目は13:20から、4時限目は15:10から、5時限目は17:00から、6時限目は18:50から
# key=1に時間表示、key=2に各時限開始までの残り時間を表示

layout = [[sg.T("00:00:00", font=("Arial",24), k="txt1")],
          [sg.ML(font=("Arial",18), size=(40,12), k="txt2")]]
win = sg.Window("時間割アプリ", layout, 
                font=(None,14), size=(450,260), keep_on_top=True)

# 時間割の定義
sch = [ ["１時限",8,50],
        ["２時限",10,30],
        ["昼休み",12,40],
        ["３時限",13,20],
        ["４時限",15,10],
        ["５時限",17,00],
        ["６時限",18,50]]

def execute():
    now = datetime.datetime.now()
    win["txt1"].update(f"{now:%H:%M:%S}")
    txt2 = ""
    for s in sch:
        dt = now.replace(hour=s[1], minute=s[2], second=0) - now
        if dt.total_seconds() > 0:
            txt2 += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】あと {dt}です。\n"
        else:
            txt2 += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】---\n"
    win["txt2"].update(txt2)

while True:
    e, v = win.read(timeout=500)
    if e == None:
        break
    execute()
win.close()