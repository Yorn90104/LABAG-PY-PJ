import tkinter as tk
from LabaModule.Var import BG , QST , picture 
from LabaModule.Sound import Ding

def setup_frame(win):
    """設置畫面"""
    Frame = tk.Frame(win, width=450, height=800, bg='lightblue')
    Canvas = tk.Canvas(Frame, width=450, height=800)
    Canvas.pack(fill="both", expand=True)
    Canvas.create_image(0, 0, image = BG, anchor="nw")
    return Frame, Canvas

def load_pic(CANVA, pc, x, y , tg):
    """加載新的圖片並放在CANVA上 (畫面 , 照片, 水平座標, 垂直座標, 標記)"""
    pic = CANVA.create_image(x, y, image = pc, anchor = "nw" , tag = tg)
    return pic

def update_pic(CANVA , tg ,  pc) :
    """更新CANVA上的圖片 (畫面, 標記, 圖)"""
    CANVA.itemconfig(tg , image = pc)

def init(CANVA, score, times, ed):
    update_pic(CANVA , "LP" , QST)
    update_pic(CANVA , "MP" , QST)
    update_pic(CANVA , "RP" , QST)

    CANVA.itemconfig("Add", text=f"")
    CANVA.itemconfig("Score", text= f"目前分數：{score}")
    CANVA.itemconfig("Times", text= f"剩餘次數：{times - ed}")

def PrizePIC(p):
    """根據歸屬選擇圖 (歸屬)"""
    if p == "A":
        return picture[0]
    elif p == "B":
        return picture[1]
    elif p == "C":
        return picture[2]
    elif p == "D":
        return picture[3]
    elif p == "E":
        return picture[4]
    elif p == "F":
        return picture[5]

def change_picture(CANVA , tg , p):
    """哪個變圖 (畫面, 標籤, 歸屬)"""
    new_pic = PrizePIC(p)
    update_pic(CANVA, tg , new_pic)
    Ding()

def Button(win , CMD , CANVA,  x , y , img):
    """添加按鈕(視窗,執行動作,畫面,水平位置,垂直位置)"""
    but = tk.Button(win , image = img , command = CMD)
    CANVA.create_window(x , y , window = but)
    return but

def Text(CANVA , x , y , txt , size , color , tg):
    """添加粗體文字(畫面,水平位置,垂直位置,大小,顏色,標記)"""
    txt = CANVA.create_text(x, y, text = txt , font = ("Arial", size , "bold") , fill = color , tag = tg)
    return txt

def result_txt(CANVA , score, add, ed, times):
    """顯示結果文字"""
    CANVA.itemconfig("Add", text= f"+{add}")
    CANVA.itemconfig("Score", text= f"目前分數：{score}")
    CANVA.itemconfig("Times", text= f"剩餘次數：{times - ed}")



