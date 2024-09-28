import sys
sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk
import pygame

# 初始化音效
pygame.mixer.init()

# 主視窗
win = tk.Tk()
win.title("啦八機")
win.iconbitmap('.\\Asset\\Superhhh.ico')
win.geometry("450x800")
win.resizable(False, False)

from LabaModule.UI import setup_frame ,  Load_PIC , Button , Text
from LabaModule.Var import score , times , ed , Title , QST , L_PIC , M_PIC , R_PIC , text_ADD , text_Score , text_Times

frame_Game, canvas_Game = setup_frame(win)
frame_End, canvas_End =setup_frame(win)

#GAME畫面
pic_Title = Load_PIC(canvas_Game , Title , 0 , 25 , "TITLE")

L_PIC = Load_PIC(canvas_Game , QST, 0, 250 , "LP")
M_PIC = Load_PIC(canvas_Game , QST, 150, 250 , "MP")
R_PIC = Load_PIC(canvas_Game , QST, 300, 250 , "RP")

text_ADD = Text(canvas_Game , 225 , 475 , "" , 16 , "yellow" , "Add")
text_Score = Text(canvas_Game , 225 , 500 , f"目前分數：{score}" , 16 , "white" , "Score")
text_Times = Text(canvas_Game , 225 , 525 , f"剩餘次數：{times - ed}" , 16 , "white" , "Times")

from LabaModule.Logic import Begin
button_Begin = Button(win , lambda :Begin(win , canvas_Game) , canvas_Game , 225 , 575)
# 綁定 Enter 鍵啟動遊戲
win.bind('<Return>', lambda event :Begin(win , canvas_Game))


frame_Game.pack(fill='both', expand=True)

win.mainloop()