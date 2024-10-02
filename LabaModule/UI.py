import tkinter as tk

from LabaModule.Var import (
                            BG,
                            QST
                            )

def setup_frame(win, tg=""):
    """設置畫面"""
    Frame = tk.Frame(win, width=450, height=800, bg='lightblue')
    Canvas = tk.Canvas(Frame, width=450, height=800)
    Canvas.pack(fill="both", expand=True)
    Canvas.create_image(0, 0, image = BG, anchor="nw", tag= tg)
    return Frame, Canvas

def load_pic(CANVA, pc, x = 0, y = 0 , tg = ""):
    """加載新的圖片並放在CANVA上 (畫面 , 照片, 水平座標, 垂直座標, 標記)"""
    CANVA.create_image(x, y, image = pc, anchor = "nw" , tag = tg)
   
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

def img_button(win , CMD , CANVA , img, x = 0, y = 0, rel = "raised", highlight = 1):
    """添加按鈕(視窗,執行動作,畫面,水平位置,垂直位置,三圍邊框效果,)"""
    but = tk.Button(
                    win ,
                    image = img ,
                    command = CMD,
                    relief =  rel,
                    highlightthickness = highlight
                    )
    CANVA.create_window(x , y , window = but)
    return but

def txt_button(win , CMD , CANVA, txt, w, h, x = 0, y = 0, size = 12, font_color = "black", bg_color = "white",tg = None):
    """添加按鈕(視窗,執行動作,畫面,水平位置,垂直位置,大小,文字顏色,背景顏色,標籤)"""
    but = tk.Button(
                    win ,
                    text = txt ,
                    command = CMD,
                    font = ("Arial", size, "bold"),
                    fg = font_color,
                    bg = bg_color
                             )
    if tg is not None:
        but.tag = tg

    # 按钮的位置&像素大小
    but.place(x=x, y=y, width=w, height=h)

    return but

def Text(CANVA , x , y , txt , size = 12 , color = "white" , tg = "", align = "center"):
    """添加粗體文字(畫面,水平位置,垂直位置,大小,顏色,標記,對齊方式[東南西北])"""
    CANVA.create_text(
                            x,
                            y,
                            text = txt ,
                            font = ("Arial", size , "bold") ,
                            fill = color ,
                            tag = tg,
                            anchor = align
                            )
    
def result_txt(CANVA , score, add, ed, times):
    """顯示結果文字"""
    CANVA.itemconfig("Add", text= f"+{add}")
    CANVA.itemconfig("Score", text= f"目前分數：{score}")
    CANVA.itemconfig("Times", text= f"剩餘次數：{times - ed}")

def delete_button(btn):
    """删除按钮"""
    btn.destroy()

def input_box(win, CANVA ,txt ="", x = 0, y = 0, size = 16, Width = 12) :
    """文字輸入盒(視窗,畫面,提示文字,水平座標,垂直座標,文字大小,寬度)"""
    entry = tk.Entry(win, width = Width, font=("Arial", size))
    entry.insert(0, txt) 
    CANVA.create_window(x, y, window = entry)
    return entry

def get_input(box = tk.Entry):
    user_input = box.get()
    return user_input