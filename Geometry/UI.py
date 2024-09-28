import tkinter as tk
from Geometry.Var import BG , QST ,L_PIC , M_PIC , R_PIC , BeginPIC , picture
from Geometry.Sound import Ding

def setup_game_frame(win):
    """設置遊戲畫面"""
    Frame_Game = tk.Frame(win, width=450, height=800, bg='lightblue')
    Canvas_Game = tk.Canvas(Frame_Game, width=450, height=800)
    Canvas_Game.pack(fill="both", expand=True)
    Canvas_Game.create_image(0, 0, image = BG, anchor="nw")
    return Frame_Game, Canvas_Game

def setup_end_frame(win):
    """設置遊戲結束畫面"""
    Frame_End = tk.Frame(win, width=450, height=800, bg='lightgreen')
    Canvas_End = tk.Canvas(Frame_End, width=450, height=800)
    Canvas_End.pack(fill="both", expand=True)
    Canvas_End.create_image(0, 0, image = BG, anchor="nw")
    return Frame_End, Canvas_End

def Load_PIC(CANVA, pc, x, y):
    """加載新的圖片並放在CANVA上 (畫面 , 照片, 水平座標, 垂直座標)"""
    CANVA.create_image(x, y, image = pc, anchor = "nw")

def Update_PIC(CANVA , n ,  pc) :
    """更新CANVA上的圖片 (畫面, 位置, 圖)"""
    CANVA.itemconfig(n , image = pc)

def init_game(CANVA):
    Update_PIC(CANVA ,L_PIC, QST)
    Update_PIC(CANVA ,M_PIC, QST)
    Update_PIC(CANVA ,R_PIC, QST)

def PIC(p):
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

def Local(CANVA , L, p):
    """哪個位置變圖 (畫面, 位置, 歸屬)"""
    new_pic = PIC(p)
    if new_pic is not None:  # 確保圖片不為 None
        Update_PIC(CANVA, L, new_pic)
    else:
        print("圖片加載失敗")

def Button(win , CMD , CANVA,  x , y):
    """添加按鈕(視窗,執行動作,畫面,水平位置,垂直位置)"""
    but = tk.Button(win , image = BeginPIC , command = CMD)
    button = CANVA.create_window(x , y , window = but)
    return button

def Text(CANVA , x , y , txt , size , color):
    """添加粗體文字(畫面,水平位置,垂直位置,大小,顏色)"""
    CANVA.create_text(x, y, text = txt , font = ("Arial", size , "bold") , fill = color)

